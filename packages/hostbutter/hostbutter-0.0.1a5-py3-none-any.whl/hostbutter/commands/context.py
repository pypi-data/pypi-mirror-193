from __future__ import annotations

import os
from typing import Any

import myke
import yapx

from ..query import _exec_docker_json_query, _print_results


def context_ls(
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
    jq.insert(
        0,
        (
            # r'.[] | select(.DockerEndpoint | startswith("ssh://"))'
            r".[] | select(.DockerEndpoint)"
            r" | {Name: .Name, DockerEndpoint: .DockerEndpoint}"
        ),
    )

    results: Any = _exec_docker_json_query(
        cmd=["context", "ls"],
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


def context_current(
    from_env: bool = yapx.arg(False, flags=["-e", "--from-env"]),
    _echo: bool = True,
) -> str:
    ctx: str | None = os.getenv("DOCKER_CONTEXT") if from_env else None

    if not ctx:
        default_context: str = "default"

        try:
            ctx = myke.read.json(os.environ["DOCKER_CONFIG_FILE"]).get(
                "currentContext",
                default_context,
            )
        except FileNotFoundError:
            ctx = default_context

        assert ctx

    if _echo:
        print(ctx)

    return ctx


def context_default(name: str = yapx.arg(pos=True)):
    myke.run(
        ["docker", "context", "use", name],
        env_update={"DOCKER_CONTEXT": "default"},
    )
