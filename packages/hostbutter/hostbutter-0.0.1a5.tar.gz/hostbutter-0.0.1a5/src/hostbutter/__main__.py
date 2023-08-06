from __future__ import annotations

import os
import sys

import myke
import yapx

from .__version__ import __version__
from .commands.ci import ci_secrets, ci_template, ci_url
from .commands.cluster import (
    cluster_create,
    cluster_edit,
    cluster_exec,
    cluster_groups,
    cluster_ls,
    cluster_ping,
    cluster_playbook,
    cluster_query,
    cluster_setup,
    cluster_ssh,
)
from .commands.context import context_current, context_default, context_ls
from .commands.registry import (
    registry_image_tags,
    registry_images,
    registry_import,
    registry_login,
    registry_ls,
)
from .commands.service import (
    service_health,
    service_logs,
    service_ls,
    service_ps,
    service_restart,
    service_scale,
    service_ssh,
)
from .commands.stack import (
    stack_build,
    stack_config,
    stack_create,
    stack_down,
    stack_ls,
    stack_ps,
    stack_secrets,
    stack_up,
    stack_update,
    stack_wait,
)
from .commands.swarm import (
    swarm_exec,
    swarm_labels,
    swarm_networks,
    swarm_nodes,
    swarm_ping,
    swarm_prune,
    swarm_query,
    swarm_reboot,
    swarm_ssh,
    swarm_stats,
)
from .query import _exec_json_query, _print_results
from .utils import set_env

ANSIBLE_COLLECTION_DIR: str = os.path.join(os.path.dirname(__file__), "collections")
ANSIBLE_REQUIREMENTS_FILE: str = os.path.join(
    ANSIBLE_COLLECTION_DIR,
    "requirements.yml",
)


def setup(
    cluster: str
    | None = yapx.arg(None, env="DOCKER_CONTEXT", flags=["-c", "--cluster"]),
    inventory_dir: str
    | None = yapx.arg(
        None,
        env="HOSTBUTTER_INVENTORY_DIR",
        flags=["-i", "--inventory"],
    ),
    docker_config: str | None = yapx.arg(None, env="DOCKER_CONFIG"),
):
    if not docker_config:
        docker_config = os.path.join(os.path.expanduser("~"), ".docker")

    docker_config_file: str = os.path.join(docker_config, "config.json")

    with set_env(
        **{
            "DOCKER_CONFIG": docker_config,
            "DOCKER_CONFIG_FILE": docker_config_file,
        },
    ):
        if not cluster:
            cluster = context_current(from_env=True, _echo=False)
            assert cluster

        if not inventory_dir:
            inventory_dir = os.path.join(os.path.expanduser("~"), ".hostbutter")

        ansible_inv_file: str = os.path.join(inventory_dir, cluster, "inventory.yml")

        with set_env(
            **{
                "DOCKER_CONTEXT": cluster,
                "ANSIBLE_INVENTORY": ansible_inv_file,
            },
        ):
            yield


def install_playbooks():
    myke.run(
        ["ansible-galaxy", "role", "install", "-r", ANSIBLE_REQUIREMENTS_FILE],
    )
    myke.run(
        ["ansible-galaxy", "collection", "install", "-r", ANSIBLE_REQUIREMENTS_FILE],
    )
    myke.run(
        [
            "ansible-galaxy",
            "collection",
            "install",
            "--force",
            os.path.join(
                ANSIBLE_COLLECTION_DIR,
                "ansible_collections",
                "fresh2dev",
                "hostbutter",
            ),
        ],
    )


def sh_exec(command: str):
    myke.run(command)


def sh_json(
    command: str,
    jq: list[str] | None = None,
    select: list[str] | None = None,
    drop: list[str] | None = None,
    extract: str | None = None,
    sort: list[str] | None = None,
    sort_reverse: bool = False,
    unique: bool = False,
    no_table: bool = yapx.arg(False, flags=["-T", "--no-table"]),
    pretty: bool = False,
    raw: bool = False,
    _echo: bool = True,
):
    results = _exec_json_query(
        cmd=command,
        jq=jq,
        select=select,
        drop=drop,
        extract=extract,
        sort=sort,
        sort_reverse=sort_reverse,
        unique=unique,
    )

    if _echo:
        if extract:
            raw = True
        _print_results(results, no_table=no_table, pretty=pretty, raw=raw)

    return results


# def registry_ls():
#     myke.read.json(os.environ["DOCKER_CONFIG_FILE"])

# def tmp_reg_creds():
#     myke.echo.pretty(myke.read.json(os.environ["DOCKER_CONFIG_FILE"]))


# TODO: implement
# def stack-catalog:
# def ci-(url|secrets|template|deploy):
# organize/segment code into private/public
# THEN, retire .hostbutter.bashrc


def main() -> None:
    args: list[str] = sys.argv[1:]
    yapx.run(
        setup,
        cluster_playbook,
        cluster_setup,
        cluster_groups,
        cluster_query,
        cluster_create,
        cluster_edit,
        cluster_ls,
        cluster_ping,
        cluster_exec,
        cluster_ssh,
        context_ls,
        context_current,
        context_default,
        swarm_stats,
        swarm_ssh,
        swarm_nodes,
        swarm_labels,
        swarm_ping,
        swarm_exec,
        swarm_prune,
        swarm_reboot,
        swarm_networks,
        stack_ls,
        stack_ps,
        stack_config,
        stack_build,
        stack_up,
        stack_down,
        stack_wait,
        stack_secrets,
        stack_update,
        stack_create,
        service_logs,
        service_ls,
        service_ps,
        service_restart,
        service_ssh,
        service_scale,
        service_health,
        registry_login,
        registry_ls,
        registry_images,
        registry_import,
        registry_image_tags,
        ci_url,
        ci_template,
        ci_secrets,
        docker=swarm_query,
        sh=sh_exec,
        sh_json=sh_json,
        version=lambda: print(__version__),
        install=install_playbooks,
        _args=args,
        _print_help="--help-full" in args,
    )


if __name__ == "__main__":
    main()
