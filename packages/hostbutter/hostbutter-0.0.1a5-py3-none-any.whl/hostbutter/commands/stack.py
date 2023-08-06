from __future__ import annotations

import os
from dataclasses import dataclass
from functools import lru_cache
from getpass import getuser
from time import time

import myke
import packaging.version
import yapx

from ..constants import STACK_NAME_VAR
from ..query import _exec_docker_json_query, _print_results
from ..utils import current_commit_sha, set_cwd, set_env
from .ci import ci_secrets, current_project_name
from .context import context_current
from .registry import _get_default_registry, registry_import
from .service import service_ps
from .swarm import swarm_ssh


def _kaniko_cli(
    src_registry: str | None = None,
    force_remote_build: bool = False,
) -> str:
    ctx: str = context_current(from_env=True, _echo=False)
    ctx_ssh: str = swarm_ssh(name=ctx, dry_run=True, _echo=False)

    if not src_registry:
        src_registry = _get_default_registry(ctx)

    tar_cmd: str = ""

    if force_remote_build or not ctx_ssh.startswith("unix://"):
        tar_args: list[str] = ["--exclude='.[^/]*'"]
        if os.path.exists(".dockerignore"):
            tar_args.append("--exclude-from='.dockerignore'")
        tar_args.extend(["-cvf", "-", "."])
        tar_cmd = f"COPYFILE_DISABLE=true tar {' '.join(tar_args)} | gzip -9 | \\"

    return (
        tar_cmd
        + r"""
        docker run --rm -i \
            -v /etc/ssl/certs/ca-certificates.crt:/etc/ssl/certs/ca-certificates.crt:ro \
            -v "${DOCKER_CONFIG:-$HOME/.docker}/config.json:/.docker/config.json"
        """.strip()
        + (" -v $(pwd):/workspace" if not tar_cmd else "")
        + f" -e DOCKER_CONFIG=/.docker {src_registry}/kaniko-project/executor:v1.9.1"
        + " --context "
        + ("tar://stdin" if tar_cmd else "dir:///workspace")
        + " "
    )


# TODO: refactor so this not called multiple times
# @lru_cache
def _get_stack_name(path: str | None = None, domain: str | None = None) -> str:
    if path and os.path.sep not in path and not os.path.isdir(path):
        return path

    env_file: str = os.path.join(path if path else os.getcwd(), ".env")

    stack_name: str | None = (
        myke.read.envfile(env_file).get(STACK_NAME_VAR).strip().lower()
    )

    if not stack_name:
        raise KeyError(f"{STACK_NAME_VAR} not defined in {env_file}")

    if domain and context_current(from_env=True, _echo=False) != domain:
        # if context is not equal to domain,
        # prepend domain to stack name.
        stack_name = domain.replace(".", "-") + "_" + stack_name

    return stack_name


def stack_wait(
    names: list[str] | None = yapx.arg(None, pos=True),
    timeout: int = 300,
    suppress_errors: bool = False,
) -> None:
    if not names:
        names = [os.getcwd()]

    stack_wait_script: str = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "resources",
        "docker-stack-wait.sh",
    )
    names = [
        _get_stack_name(x) if (os.path.sep in x or os.path.isdir(x)) else x
        for x in names
    ]

    for x in names:
        myke.run(
            [
                "sh",
                stack_wait_script,
                "-t",
                str(timeout),
                "-p",
                "10",
                x,
            ],
            check=(not suppress_errors),
        )


@dataclass
class _StackEnv:
    name: str | None = None
    domain: str | None = None
    image_registry: str | None = None
    image_owner: str | None = None
    image_tag: str | None = None
    nfs_opts: str | None = None

    def __post_init__(self):
        if not self.domain:
            self.domain = os.getenv("HB_DOMAIN", os.environ["DOCKER_CONTEXT"])

        self.name = _get_stack_name(path=self.name, domain=self.domain)

        if not self.image_registry:
            self.image_registry = os.getenv(
                "HB_IMAGE_REGISTRY",
                "registry." + self.domain,
            )

        if not self.image_owner:
            self.image_owner = os.getenv("HB_IMAGE_OWNER", getuser())

        if not self.image_tag:
            self.image_tag = current_commit_sha()

        if not self.nfs_opts:
            self.nfs_opts = os.getenv(
                "HB_NFS_OPTS",
                f"addr=nas.{self.domain},vers=4.1,rw",
            )

    def to_dict(self) -> dict[str, str]:
        assert self.domain
        assert self.name
        assert self.image_registry
        assert self.image_owner
        assert self.image_tag
        assert self.nfs_opts

        stack_env: dict[str, str] = {
            "COMPOSE_PROJECT_NAME": self.name,
            "HB_DOMAIN": self.domain,
            "HB_IMAGE_REGISTRY": self.image_registry,
            "HB_IMAGE_OWNER": self.image_owner,
            "HB_IMAGE_TAG": self.image_tag,
            "HB_NFS_OPTS": self.nfs_opts,
            "NOW": str(int(time())),
        }

        env_update_file: str = os.path.join("secrets", self.domain, ".env")
        if os.path.exists(env_update_file):
            stack_env.update(myke.read.dotfile(env_update_file))

        return stack_env


@lru_cache()
def _get_stack_env(
    name: str | None = None,
    domain: str | None = None,
    image_registry: str | None = None,
    image_owner: str | None = None,
    image_tag: str | None = None,
    nfs_opts: str | None = None,
) -> _StackEnv:
    return _StackEnv(
        name=name,
        domain=domain,
        image_registry=image_registry,
        image_owner=image_owner,
        image_tag=image_tag,
        nfs_opts=nfs_opts,
    )


def stack_config(
    path: str | None = None,
    files: list[str] | None = None,
    domain: str | None = None,
    image_registry: str | None = None,
    image_owner: str | None = None,
    nfs_opts: str | None = None,
    _echo: bool = True,
) -> str:
    if not path:
        path = os.getcwd()

    if not files:
        files = ["docker-compose.yml"]

    with set_cwd(path):
        env_update: dict[str, str] = _get_stack_env(
            name=path,
            domain=domain,
            image_registry=image_registry,
            image_owner=image_owner,
            nfs_opts=nfs_opts,
        ).to_dict()

        stdout, _stderr, _returncode = myke.run(
            (
                "(echo 'version: \"3.9\"' && DOCKER_CONTEXT=default docker compose"
                f" -f {' -f '.join(files)} config) | "
                r' sed "s/^\([[:space:]]\+name:'
                r' [a-zA-Z0-9\_\-]\+\_\)\([[:digit:]]\+\)$/\1$NOW/g"'
            ),
            env_update=env_update,
            capture_output=True,
            echo=_echo,
        )
        assert stdout

        return stdout


def stack_up(
    paths: list[str] | None = yapx.arg(None, pos=True),
    files: list[str] | None = yapx.arg(None),
    domain: str | None = yapx.arg(None, env="HB_DOMAIN"),
    image_owner: str
    | None = yapx.arg(None, flags=["-o", "--owner"], env="HB_IMAGE_OWNER"),
    image_registry: str
    | None = yapx.arg(None, flags=["-r", "--registry"], env="HB_IMAGE_REGISTRY"),
    nfs_opts: str | None = yapx.arg(None, env="HB_NFS_OPTS"),
    no_wait: bool = yapx.arg(False, flags=["-W", "--no-wait"]),
    build: bool = False,
    build_args: dict[str, str] | None = yapx.arg(None, flags=["-a", "--build-args"]),
) -> None:
    if not paths:
        paths = [os.getcwd()]

    for p in paths:
        stack_name: str = _get_stack_name(p, domain=domain)

        if build:
            with set_cwd(p):
                stack_build(
                    image_tags=None,
                    tag_version=None,
                    image_owner=image_owner,
                    target_registry=image_registry,
                    build_args=build_args,
                    force_remote_build=False,
                    no_import=False,
                )

        myke.sh(
            (
                "docker stack deploy --prune --with-registry-auth --resolve-image"
                " always --compose-file - $COMPOSE_PROJECT_NAME"
            ),
            env_update={"COMPOSE_PROJECT_NAME": stack_name},
            input=stack_config(
                p,
                files=files,
                domain=domain,
                image_registry=image_registry,
                image_owner=image_owner,
                nfs_opts=nfs_opts,
                _echo=True,
            ).encode(),
        )

    if not no_wait:
        stack_wait(paths)


def stack_down(
    names: list[str] | None = yapx.arg(None, pos=True),
    no_wait: bool = yapx.arg(False, flags=["-W", "--no-wait"]),
) -> None:
    if not names:
        names = [os.getcwd()]

    names = [_get_stack_name(x) for x in names]

    myke.run(["docker", "stack", "rm", *names])

    if not no_wait:
        stack_wait(names, suppress_errors=True)


def stack_ls(
    jq: list[str] = yapx.arg(lambda: [], flags=["-q", "--jq"]),
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
    results = _exec_docker_json_query(
        ["stack", "ls"],
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


def stack_ps(
    names: list[str] | None = yapx.arg(None, pos=True),
    all_states: bool = False,
    jq: list[str] = yapx.arg(lambda: [], flags=["-q", "--jq"]),
    select: list[str] | None = None,
    drop: list[str] | None = None,
    extract: str | None = None,
    sort: list[str] | None = None,
    sort_reverse: bool = False,
    unique: bool = False,
    no_table: bool = yapx.arg(False, flags=["-T", "--no-table"]),
    pretty: bool = False,
    raw: bool = False,
    verbose: bool = False,
    _echo: bool = True,
):
    if not names:
        names = [os.getcwd()]

    names = [_get_stack_name(x) for x in names]

    return service_ps(
        names=None,
        stacks=names,
        all_states=all_states,
        jq=jq,
        select=select,
        drop=drop,
        extract=extract,
        sort=sort,
        sort_reverse=sort_reverse,
        unique=unique,
        no_table=no_table,
        pretty=pretty,
        raw=raw,
        verbose=verbose,
        _echo=_echo,
    )


def stack_build(
    image_tags: list[str] | None = yapx.arg(None, flags=["-t", "--tag", "--tags"]),
    tag_version: str | None = yapx.arg(None, flags=["--tag-version"]),
    image_owner: str
    | None = yapx.arg(None, flags=["-o", "--owner"], env="HB_IMAGE_OWNER"),
    target_registry: str
    | None = yapx.arg(None, flags=["-r", "--registry"], env="HB_IMAGE_REGISTRY"),
    build_args: dict[str, str] | None = yapx.arg(None, flags=["-a", "--build-args"]),
    force_remote_build: bool = yapx.arg(False, flags=["--force-remote-build"]),
    no_import: bool = yapx.arg(False, flags=["-I", "--no-import"]),
):
    if not target_registry:
        target_registry = _get_default_registry()

    if not no_import:
        image_import_file: str = "images.txt"
        if os.path.exists(image_import_file):
            registry_import(
                import_file=image_import_file,
                image_names=None,
                new_registry=target_registry,
                new_owner=None,
                all_tags=False,
                skopeo_image_registry=None,
            )

    tag_list: list[str] = [current_commit_sha()]

    if tag_version:
        tag_list.append(tag_version)
        try:
            version = packaging.version.parse(tag_version)
            if not any(
                [version.is_devrelease, version.is_prerelease, version.is_postrelease],
            ):
                for i in 3, 2, 1:
                    if i <= len(version.release):
                        v: str = ".".join(str(x) for x in version.release[:i])
                        if v and v not in tag_list:
                            tag_list.append(v)
        except packaging.version.InvalidVersion:
            pass

    if image_tags:
        tag_list.extend(image_tags)

    if not image_owner:
        image_owner = getuser()

    destinations: str = "--destination " + " --destination ".join(
        f"{target_registry}/{image_owner}/{_get_stack_name()}:{x}" for x in tag_list
    )

    if not build_args:
        build_args = {}

    build_args["HB_IMAGE_REGISTRY"] = target_registry

    build_args_str: str = " ".join(
        f"--build-arg {k}={v}" for k, v in build_args.items()
    )

    myke.run(
        _kaniko_cli(force_remote_build=force_remote_build)
        + f"--build-arg HB_IMAGE_REGISTRY='{target_registry}'"
        f" {build_args_str} {destinations}",
    )


def stack_create(
    directory: str,
    minimal: bool = False,
    pre_release: bool = yapx.arg(False, flags=["--pre", "--pre-release"]),
    answers: dict[str, str] | None = None,
    template_repo: str = yapx.arg(
        "https://codeberg.org/Fresh2dev/copier-f2dv-project.git",
        flags=["-r", "--repo"],
    ),
    dry_run: bool = False,
    force: bool = False,
):
    copier_args: list[str] = ["--overwrite"]

    if dry_run:
        copier_args.append("--pretend")

    if pre_release:
        copier_args.extend(["--vcs-ref", "dev"])

    if not force and os.path.exists(directory) and os.listdir(directory):
        raise FileExistsError("Refusing to target non-empty directory: " + directory)

    copier_answers: dict[str, str] = {
        "is_python": "false",
        "is_minimal": "true" if minimal else "false",
    }

    if answers:
        copier_answers.update(answers)

    copier_args.extend(
        x for k, v in copier_answers.items() for x in ["--data", f"{k}={v}"]
    )

    myke.run(
        ["copier"]
        + copier_args
        + ["copy"]
        + ["--no-cleanup", template_repo, directory],
        env_update={"HOME": "/dev/null"},
    )


def stack_update(
    answers: dict[str, str] | None = None,
    pre_release: bool = yapx.arg(False, flags=["-p", "--pre", "--pre-release"]),
    clobber: bool = False,
    dry_run: bool = False,
):
    copier_answers = myke.read.yaml(".copier-answers.yml")
    template_repo: str = copier_answers.pop("_src_path")
    copier_answers = {k: v for k, v in copier_answers.items() if not k.startswith("_")}

    if answers:
        copier_answers.update(answers)

    if clobber:
        stack_create(
            directory=os.getcwd(),
            pre_release=pre_release,
            answers=copier_answers,
            template_repo=template_repo,
            dry_run=dry_run,
            force=True,
        )
    else:
        copier_args: list[str] = ["--overwrite"]

        if dry_run:
            copier_args.append("--pretend")

        if pre_release:
            copier_args.extend(["--vcs-ref", "dev"])

        copier_args.extend(
            x for k, v in copier_answers.items() for x in ["--data", f"{k}={v}"]
        )

        myke.run(
            ["copier"] + copier_args + ["update"],
            env_update={"HOME": "/dev/null"},
        )

    if not dry_run:
        myke.run("find . -name '*.rej' -delete;")

        print("Pulled latest modifications. Running pre-commit...\n")
        myke.run("git pre-commit --all-files", echo=False, check=False)
        print("Update complete. Review changes before committing.\n")


def stack_secrets(
    vault_server: str = yapx.arg(env=["HB_VAULT_ADDR", "VAULT_ADDR"]),
    vault_api_token: str = yapx.arg(env=["HB_VAULT_TOKEN", "VAULT_TOKEN"]),
    get_secrets: bool = yapx.arg(False, exclusive=True, flags=["--get"]),
    put_secrets: bool = yapx.arg(False, exclusive=True, flags=["--put"]),
    put_all_secrets: bool = yapx.arg(False, exclusive=True, flags=["--put-all"]),
    domains: list[str] | None = yapx.arg(None, env="HB_DOMAIN"),
    secrets_dir: str = "secrets",
    vault_root_path: str | None = "secret/hostbutter",
):
    if not os.path.exists(secrets_dir):
        raise FileNotFoundError(secrets_dir)

    if put_all_secrets:
        put_secrets = True
        if not domains:
            domains = os.listdir(secrets_dir)
    elif not domains:
        domains = [os.environ["DOCKER_CONTEXT"]]

    with set_env(VAULT_ADDR=vault_server, VAULT_TOKEN=vault_api_token):
        for d in domains:
            domain_secrets = os.path.join(secrets_dir, d)

            vault_path = f"projects/{d}/{current_project_name()}"

            if get_secrets:
                ci_secrets(
                    vault_server=vault_server,
                    vault_api_token=vault_api_token,
                    get_secrets=True,
                    put_secrets=None,
                    patch_secrets=None,
                    scope=None,
                    vault_path=vault_path,
                    vault_root_path=vault_root_path,
                )
            elif put_secrets:
                secret_files: dict[str, str] = {
                    x: "@" + os.path.join(domain_secrets, x)
                    for x in os.listdir(domain_secrets)
                    if os.path.isfile(x)
                }

                if secret_files:
                    ci_secrets(
                        vault_server=vault_server,
                        vault_api_token=vault_api_token,
                        get_secrets=False,
                        put_secrets=secret_files,
                        patch_secrets=None,
                        scope=None,
                        vault_path=vault_path,
                        vault_root_path=vault_root_path,
                    )
            else:
                print("Specify '--get' or '--put'")
                break
