from __future__ import annotations

import os
import sys

import myke
import yaml
import yapx

from ..__version__ import __version__
from ..exceptions import NoKnownCiServerError, NoKnownDnsServerError
from ..utils import current_project_name, set_env
from .context import context_current
from .registry import _get_default_registry

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


def _get_default_ci_server(context: str | None = None) -> str:
    reg: str | None = os.getenv("DRONE_SERVER")

    if not reg:
        if not context:
            context = context_current(from_env=True, _echo=False)

        if "." not in context:
            raise NoKnownCiServerError(
                "Unable to infer CI server URL within current context: " + context,
            )

        reg = "ci." + context

    return reg


def ci_url(
    # ci_api_token: str = yapx.arg(env=['HB_CI_TOKEN', 'DRONE_TOKEN']),
    ci_server: str
    | None = yapx.arg(None, env=["HB_CI_SERVER", "DRONE_SERVER"]),
):
    with set_env(DRONE_SERVER=ci_server):
        if not ci_server:
            ci_server = _get_default_ci_server()

        if not ci_server.startswith("https://"):
            ci_server = "https://" + ci_server

        print(f"{ci_server.rstrip('/')}/{current_project_name()}")


def ci_template(
    image_registry: str
    | None = yapx.arg(None, flags=["-r", "--registry"], env="HB_IMAGE_REGISTRY"),
    dns_servers: list[str] | None = yapx.arg(None, flags=["--dns", "--dns-servers"]),
):
    if not dns_servers:
        with open(os.environ["ANSIBLE_INVENTORY"], encoding="utf-8") as f:
            dns_servers = (
                yaml.safe_load(f)
                .get("all", {})
                .get("vars", {})
                .get("dnsmasq_dns_servers")
            )

        if not dns_servers:
            raise NoKnownDnsServerError()

    if not image_registry:
        image_registry = _get_default_registry()

    myke.echo.text(
        myke.read.text(
            os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                "resources",
                "hostbutter.jsonnet",
            ),
        )
        .replace("%HB_IMAGE_REGISTRY%", image_registry, 1)
        .replace("%HB_CI_DNS%", "', '".join(x.strip("'\",") for x in dns_servers), 1)
        .replace("%HB_VERSION%", __version__, 1),
    )


def ci_secrets(
    vault_server: str = yapx.arg(env=["HB_VAULT_ADDR", "VAULT_ADDR"]),
    vault_api_token: str = yapx.arg(env=["HB_VAULT_TOKEN", "VAULT_TOKEN"]),
    get_secrets: bool = yapx.arg(False, exclusive=True, flags=["--get"]),
    put_secrets: dict[str, str]
    | None = yapx.arg(None, exclusive=True, flags=["--put"]),
    patch_secrets: dict[str, str]
    | None = yapx.arg(None, exclusive=True, flags=["--patch"]),
    scope: Literal["global", "cluster"] | None = None,
    vault_path: str | None = None,
    vault_root_path: str | None = "secret/hostbutter",
):
    vault_root_path.rstrip("/")

    if scope == "global":
        vault_root_path = f"{vault_root_path}/global"
    elif scope == "cluster":
        vault_root_path = f"{vault_root_path}/clusters/{os.environ['DOCKER_CONTEXT']}"

    if not vault_path:
        vault_path = vault_root_path
    else:
        vault_path = f"{vault_root_path}/{vault_path.lstrip('/')}"

    if patch_secrets:
        put_secrets = patch_secrets

    with set_env(VAULT_ADDR=vault_server, VAULT_TOKEN=vault_api_token):
        if get_secrets:
            myke.run(["vault", "kv", "get", "-format=yaml", vault_path], check=False)
        elif put_secrets:
            myke.run(
                [
                    "vault",
                    "kv",
                    "patch" if patch_secrets else "put",
                    "--non-interactive",
                    vault_path,
                ]
                + [f"{k}={v}" for k, v in put_secrets.items()],
                check=False,
            )
        else:
            print("Specify '--get' or '--put'")
