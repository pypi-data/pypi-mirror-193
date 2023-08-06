from __future__ import annotations

from typing import Any

import myke
import yapx

from ..query import _exec_docker_json_query, _jq_query, _print_results


def service_logs(name: str):
    myke.run(["docker", "service", "logs", "-f", "--tail", "100", name])


def service_restart(names: list[str] = yapx.arg(pos=True)):
    for x in names:
        myke.run(
            [
                "docker",
                "service",
                "update",
                "--force",
                "--with-registry-auth",
                "--update-parallelism",
                "0",
                x,
            ],
        )


def service_scale(
    names: list[str] = yapx.arg(pos=True),
    replicas: int = yapx.arg(),
    no_wait: bool = yapx.arg(False, flags=["-W", "--no-wait"]),
):
    myke.run(
        [
            "docker",
            "service",
            "scale",
        ]
        + (["--detach"] if no_wait else [])
        + [f"{x}={replicas}" for x in names],
    )


def service_ls(
    stack: str | None = yapx.arg(None, pos=True),
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
    if not verbose and not select:
        select = ["Name", "Mode", "Replicas"]

    results = _exec_docker_json_query(
        ["service", "ls"]
        + (["--filter", "label=com.docker.stack.namespace=" + stack] if stack else []),
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


def service_ps(
    names: list[str] | None = yapx.arg(None, pos=True, exclusive=True),
    stacks: list[str] | None = yapx.arg(None, exclusive=True),
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
    if not verbose and not select:
        select = ["Name", "DesiredState", "CurrentState", "Node", "Error"]

    if not names:
        if stacks:
            names = [
                y
                for x in stacks
                for y in service_ls(
                    stack=x,
                    jq=[],
                    no_table=True,
                    extract="Name",
                    _echo=False,
                )
            ]
        else:
            names = service_ls(jq=[], no_table=True, extract="Name", _echo=False)
    elif isinstance(names, str):
        names = [names]

    assert names
    names.sort()

    state_filters: list[str] = (
        []
        if all_states
        else [
            "--filter",
            "desired-state=running",
            "--filter",
            "desired-state=ready",
            "--filter",
            "desired-state=accepted",
        ]
    )

    results = _exec_docker_json_query(
        ["service", "ps", "--no-trunc"] + state_filters + names,
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


def _service_node_containers(name: str) -> list[tuple[str, str]]:
    return [
        (node, container["ID"])
        for node in service_ps(
            [name],
            stacks=None,
            jq=[],
            no_table=True,
            extract="Node",
            _echo=False,
        )
        for container in _exec_docker_json_query(
            [
                "ps",
                "--filter",
                "label=com.docker.swarm.service.name=" + name,
            ],
            env_update={"DOCKER_CONTEXT": node},
        )
    ]


def service_health(
    name: str = yapx.arg(pos=True),
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
    results: list[dict[str, Any]] = [
        c_info
        for node, c_id in _service_node_containers(name)
        for c_info in _exec_docker_json_query(
            [
                "inspect",
                c_id,
            ],
            env_update={"DOCKER_CONTEXT": node},
        )
    ]

    results = _jq_query(
        records=results,
        expr=[r".[] | {ID: .Id, Name: .Name, RestartCount: .RestartCount} + .State"]
        + jq,
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


def service_ssh(name: str = yapx.arg(pos=True), shell: str = "sh"):
    for node, c_id in _service_node_containers(name):
        print(f"\n*** {node}: {c_id}\n")
        myke.run(
            ["docker", "exec", "-it", c_id, shell],
            env_update={"DOCKER_CONTEXT": node},
        )
