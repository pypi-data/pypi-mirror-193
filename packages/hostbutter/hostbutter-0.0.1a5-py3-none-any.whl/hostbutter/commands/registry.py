from __future__ import annotations

import json
import os
from fnmatch import fnmatch
from getpass import getpass
from typing import Any

import myke
import requests
import yapx

from ..constants import CI_IMAGE_DEPENDENCIES, IMAGE_DEPENDENCIES
from ..exceptions import NoKnownRegistryError, NoTagsFoundError, TooManyTagsError
from ..query import _exec_json_query, _jq_query, _print_results
from .context import context_current
from .swarm import swarm_ssh

REGISTRY_NAME_MAP: dict[str, str] = {"docker.io": "https://index.docker.io/v1/"}


def _skopeo_cmd(skopeo_args: str | list[str], src_registry: str | None = None) -> str:
    ctx: str = context_current(from_env=True, _echo=False)

    if not src_registry:
        src_registry = _get_default_registry(ctx)

    cmd: str = (
        r"""
docker run --rm -i \
    -v /etc/ssl/certs/ca-certificates.crt:/etc/ssl/certs/ca-certificates.crt:ro \
    -v "${DOCKER_CONFIG:-$HOME/.docker}/config.json:/.docker/config.json:ro" \
    -e REGISTRY_AUTH_FILE=/.docker/config.json
""".strip()
        + f" {src_registry}/skopeo/stable:v1.9.2"
        + " "
    )

    if not isinstance(skopeo_args, str):
        skopeo_args = " ".join(skopeo_args)

    ctx_ssh: str = swarm_ssh(name=ctx, dry_run=True, _echo=False)
    if ctx_ssh.startswith("ssh://"):
        cmd = f"ssh {ctx_ssh} '{cmd} {skopeo_args}'"
    else:
        cmd += skopeo_args

    return cmd


def _get_default_registry(context: str | None = None) -> str:
    reg: str | None = os.getenv("HB_IMAGE_REGISTRY")

    if not reg:
        if not context:
            context = context_current(from_env=True, _echo=False)

        if "." not in context:
            raise NoKnownRegistryError(
                "Unable to infer registry URL within current context: " + context,
            )

        reg = "registry." + context

    return reg


def _split_image_parts(
    image_name: str,
    default_registry: str | None = None,
    default_tag: str | None = None,
) -> tuple[str, str, str | None]:
    if not default_registry:
        default_registry = "docker.io"

    image_parts: list[str] = image_name.split(":", maxsplit=1)

    image_name = image_parts[0]

    image_tag: str | None = image_parts[1] if len(image_parts) > 1 else default_tag

    image_parts = image_name.split("/", maxsplit=1)

    if len(image_parts) == 1:
        image_registry = default_registry
        image_name = image_parts[0]
    elif "." not in image_parts[0]:
        image_registry = default_registry
    else:
        image_registry = image_parts[0]
        image_name = image_parts[1]

    return image_registry, image_name, image_tag


def registry_ls(
    raw: bool = False,
    _echo: bool = True,
) -> list[dict[str, str]] | list[str]:
    ctx: str = context_current(from_env=True, _echo=False)
    ctx_ssh: str = swarm_ssh(name=ctx, dry_run=True, _echo=False)

    is_ssh_context: bool = ctx_ssh.startswith("ssh://")
    cmd: list[str] = ["ssh", ctx_ssh] if is_ssh_context else []
    cmd.append("cat ${DOCKER_CONFIG:-~/.docker}/config.json")

    stdout, _, _ = myke.run(
        cmd,
        capture_output=True,
        echo=False,
        shell=(not is_ssh_context),
    )
    assert stdout

    reg_info: dict[str, dict[str, str]] | list[dict[str, str]] | list[str] = json.loads(
        stdout,
    )

    if not raw:
        reg_info = list(reg_info["auths"].keys())

    if _echo:
        _print_results(reg_info, no_table=True, pretty=False, raw=False)

    return reg_info


def _get_registry_creds(name: str) -> str:
    results: dict[str, Any] = registry_ls(raw=True, _echo=False)

    matching: list[str] = [
        v["auth"]
        for k, v in results["auths"].items()
        if k == REGISTRY_NAME_MAP.get(name, name)
    ]

    if not matching:
        print("Unrecognized registry. Select one of:")
        registry_ls(raw=False, _echo=True)
        raise ValueError(name)

    return matching[0]


def registry_login(
    url: str | None = yapx.arg(None, pos=True, env="HB_IMAGE_REGISTRY"),
    username: str = yapx.arg(None, env="HB_IMAGE_REGISTRY_USER"),
    password: str | None = yapx.arg(None, env="HB_IMAGE_REGISTRY_PASS"),
):
    ctx: str = context_current(from_env=True, _echo=False)
    ctx_ssh: str = swarm_ssh(name=ctx, dry_run=True, _echo=False)

    if not url:
        url = _get_default_registry(ctx)

    if not username:
        username = input("Username: ")
        assert username

    if not password:
        password = getpass()
        assert password

    is_ssh_context: bool = ctx_ssh.startswith("ssh://")
    cmd: list[str] = ["ssh", ctx_ssh] if is_ssh_context else []
    cmd.append(f'docker login --username "{username}" --password-stdin {url}')

    myke.run(cmd, input=password.encode(), shell=(not is_ssh_context))


def registry_images(
    registry: str | None = yapx.arg(None, pos=True),
    img_filter: str | None = yapx.arg(None, flags=["-f", "--filter"]),
    v1_api: bool = yapx.arg(False, flags="--v1-api"),
    limit: int = yapx.arg(1000, flags=["-n", "--limit"]),
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
) -> list[str]:
    if not registry:
        registry = _get_default_registry()

    reg_url: str = REGISTRY_NAME_MAP.get(registry, registry)

    if not reg_url.startswith("https://"):
        reg_url = f"https://{reg_url}/" + ("v1" if v1_api else "v2")

    reg_url = reg_url.rstrip("/")

    is_v1_api: bool = "v1" in reg_url
    if is_v1_api:
        if not img_filter:
            raise ValueError("Image filter is required for Registry v1 API.")
        reg_url = reg_url + f"/search?q={img_filter.replace('*', '')}&n=100"
    else:
        reg_url = reg_url + "/_catalog"

    imgs: list[dict[str, str | int | bool]] = []

    limit_reached: bool = False

    page: int = 0
    num_pages: int = 0
    while not limit_reached and (page == 0 or (is_v1_api and page < num_pages)):
        resp: requests.Response = requests.get(
            reg_url + (f"&page={page+1}" if page > 0 else ""),
            headers={"Authorization": f"Basic {_get_registry_creds(name=registry)}"},
            verify=os.getenv(
                "REQUESTS_CA_BUNDLE",
                "/etc/ssl/certs/ca-certificates.crt",
            ),
            timeout=300,
        )

        resp.raise_for_status()

        resp_data: dict[str, Any] = resp.json()

        if is_v1_api:
            imgs.extend(resp_data["results"])

            page = resp_data["page"]
            num_pages = resp_data["num_pages"]
        else:
            imgs.extend({"name": x} for x in resp_data["repositories"])
            page += 1

        if img_filter:
            imgs = [x for x in imgs if fnmatch(x["name"], img_filter)]

        if limit > 0 and len(imgs) >= limit:
            limit_reached = True

    for x in imgs:
        x["name"] = f"{registry}/{x['name']}"

    if is_v1_api and not verbose and not select:
        select = [
            "name",
            "pull_count",
            "star_count",
        ]

    if not sort:
        if is_v1_api:
            sort = ["pull_count", "star_count"]
        else:
            sort = ["name"]
            sort_reverse = True

    results = _jq_query(
        records=imgs,
        expr=jq,
        select=select,
        drop=drop,
        extract=extract,
        sort=sort,
        sort_reverse=sort_reverse,
        unique=unique,
    )

    if limit_reached:
        results = results[:limit]

    if _echo:
        if extract:
            raw = True
        _print_results(results, no_table=no_table, pretty=pretty, raw=raw)

        if limit_reached:
            print(
                (
                    '...\n\n*** Result limit reached. Adjust filter ("--filter") and/or'
                    ' limit ("--limit").\n'
                ),
            )

    return results


def registry_image_tags(
    image_name: str = yapx.arg(pos=True),
    image_registry: str | None = yapx.arg(None, flags=["-r", "--registry"]),
    tag_filter: str | None = yapx.arg(None, flags=["-f", "--filter"]),
    remove: bool = yapx.arg(False, flags=["--rm", "--remove"]),
    _echo: bool = True,
    _skopeo_image_registry: str | None = None,
) -> list[str]:
    new_img_registry, image_name, image_tag = _split_image_parts(
        image_name=image_name,
        default_registry=image_registry,
        default_tag=None,
    )

    if image_registry:
        new_img_registry = image_registry

    if not tag_filter and image_tag:
        tag_filter = image_tag

    image_name_fq: str = f"{new_img_registry}/{image_name}"

    results: list[str] = [
        y
        for x in _exec_json_query(
            _skopeo_cmd(
                "list-tags --retry-times 2 docker://" + image_name_fq,
                src_registry=_skopeo_image_registry,
            ),
        )
        for y in x["Tags"]
    ]

    if tag_filter:
        results = [x for x in results if fnmatch(x, tag_filter)]

    results = [f"{image_name_fq}:{x}" for x in results]

    if remove:
        for x in results:
            if _echo:
                print("Deleting image tag: " + x)
            myke.run(
                _skopeo_cmd(
                    "delete docker://" + x,
                    src_registry=_skopeo_image_registry,
                ),
            )
    elif _echo:
        myke.echo.lines(results)

    return results


def registry_import(
    image_names: list[str] | None = yapx.arg(None, pos=True, exclusive=True),
    import_file: str | None = yapx.arg(None, exclusive=True, flags=["-f", "--file"]),
    dependencies: bool | None = yapx.arg(None, exclusive=True),
    ci_dependencies: bool | None = yapx.arg(None, exclusive=True),
    new_registry: str | None = yapx.arg(None, flags=["-r", "--registry"]),
    new_owner: str | None = yapx.arg(None, flags=["-o", "--owner"]),
    all_tags: bool = yapx.arg(False, flags=["-a", "--all-tags"]),
    src_no_creds: bool = False,
    multi_arch: bool = False,
    force: bool = False,
    dry_run: bool = False,
    skopeo_image_registry: str | None = yapx.arg(None, flags=["--skopeo-registry"]),
):
    import_images: list[str] = (
        image_names
        if image_names
        else [
            y
            for x in myke.read.lines(import_file)
            for y in [x.strip()]
            if not y.startswith("#")
        ]
        if import_file
        else IMAGE_DEPENDENCIES
        if dependencies
        else CI_IMAGE_DEPENDENCIES
        if ci_dependencies
        else []
    )

    if not new_registry:
        new_registry = _get_default_registry()

    for this_image in import_images:
        src_registry, img_name, img_tag = _split_image_parts(image_name=this_image)

        src_images: list[str] = (
            [f"{src_registry}/{img_name}:{img_tag}"]
            if img_tag and "*" not in img_tag
            else registry_image_tags(
                img_name,
                image_registry=src_registry,
                tag_filter=img_tag,
                remove=False,
                _echo=False,
                _skopeo_image_registry=skopeo_image_registry,
            )
        )

        if not src_images:
            raise NoTagsFoundError(
                f"No matching tags found for image: {src_registry}/{img_name}",
            )

        if not img_tag and len(src_images) > 1 and not all_tags:
            raise TooManyTagsError(
                (
                    "No tag given and multiple tags found."
                    " Specify a tag, or use '--all-tags' to import all tags."
                ),
            )

        if new_owner:
            img_name_parts: list[str] = img_name.split("/", maxsplit=1)
            img_name = f"{new_owner}/{img_name_parts[len(img_name_parts)-1]}"

        if not skopeo_image_registry and (dependencies or ci_dependencies):
            skopeo_image_registry = "quay.io"

        tgt_images: list[str]

        try:
            tgt_images = registry_image_tags(
                img_name,
                image_registry=new_registry,
                tag_filter=None,
                remove=False,
                _echo=False,
                _skopeo_image_registry=skopeo_image_registry,
            )
        except myke.exceptions.CalledProcessError as e:
            print(e.stdout)
            print(e.stderr)
            print(e.returncode)
            tgt_images = []

        for src_img in src_images:
            _, src_tag = src_img.split(":", maxsplit=1)
            tgt_img: str = f"{new_registry}/{img_name}:{src_tag}"

            if not force and tgt_img in tgt_images:
                print("exists: " + tgt_img)
            else:
                print("import: " + tgt_img)
                if not dry_run:
                    extra_args: list[str] = ["--retry-times", "2"]
                    if src_no_creds:
                        extra_args.append("--src-no-creds")
                    if multi_arch:
                        extra_args.extend(["--multi-arch", "all"])

                    myke.run(
                        _skopeo_cmd(
                            (
                                "copy"
                                f" {' '.join(extra_args)} docker://{src_img} docker://{tgt_img}"
                            ),
                            src_registry=skopeo_image_registry,
                        ),
                    )
