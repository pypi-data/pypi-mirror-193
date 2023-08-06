from __future__ import annotations

import json
from typing import Any

import jq as _jq
import myke

from .constants import SWARM_GROUP_NAME


def _jq_query(
    records: list[dict[str, Any]],
    expr: str | list[str],
    select: list[str] | None = None,
    drop: list[str] | None = None,
    extract: str | None = None,
    sort: list[str] | None = None,
    sort_reverse: bool = False,
    unique: bool = False,
) -> Any:
    if isinstance(expr, str):
        expr = [expr]

    if sort:
        sort_expr: str = f'. | sort_by(.{", .".join(sort)})'
        if not sort_reverse:
            sort_expr += " | reverse"
        sort_expr += "[]"
        expr.append(sort_expr)

    if drop:
        expr.append(f'.[] | del(.{", .".join(drop)})')

    if select:
        expr.append(f'.[] | {{{", ".join(select)}}}')

    if extract:
        expr.append(f".[] | .{extract}")

    if unique:
        expr.append(". | unique_by(.)[]")

    for x in expr:
        records = _jq.compile(x).input(records).all()

    return records


def _print_results(
    results: Any,
    no_table: bool = False,
    pretty: bool = False,
    raw: bool = False,
) -> None:
    if results is not None:
        if no_table or (
            isinstance(results, list)
            and results
            and (not isinstance(results[0], dict) or len(results[0].keys()) > 6)
        ):
            if raw:
                myke.echo.lines(results)
            elif pretty:
                myke.echo.pretty(results)
            else:
                myke.echo.json(results, indent=2)
        elif raw:
            myke.echo.table(results, tablefmt="tsv")
        elif pretty:
            myke.echo.table(results, tablefmt="rounded_grid")
        else:
            myke.echo.table(results, tablefmt="github")


def _exec_json_query(
    cmd: str | list[str],
    jq: list[str] | None = None,
    select: list[str] | None = None,
    drop: list[str] | None = None,
    extract: str | None = None,
    sort: list[str] | None = None,
    sort_reverse: bool = False,
    unique: bool = False,
    **kwargs: Any,
) -> Any:
    if jq is None:
        jq = []

    stdout, _, _ = myke.run(cmd, capture_output=True, echo=False, **kwargs)

    records: list[dict[str, Any]]

    try:
        parsed = json.loads(stdout)
        if isinstance(parsed, dict):
            records = [parsed]
        elif isinstance(parsed, list):
            records = parsed
        else:
            raise TypeError(
                "Unsupported Json data structure; list of dictionaries expected.",
            )
    except json.JSONDecodeError:
        try:
            records = [json.loads(x) for x in stdout.splitlines()]
        except json.JSONDecodeError:
            try:
                records = [
                    {
                        **({"__hostname__": hostname} if hostname else {}),
                        **json.loads(payload),
                    }
                    for x in stdout.splitlines()
                    for i in [x.index("{")]
                    for hostname in [x[:i].split("|", maxsplit=1)[0].strip()]
                    for payload in x[i:].split("\\n")
                ]
            except json.JSONDecodeError as e:
                print(stdout[:200])
                raise e

    return _jq_query(
        records,
        expr=jq,
        select=select,
        drop=drop,
        extract=extract,
        sort=sort,
        sort_reverse=sort_reverse,
        unique=unique,
    )


def _exec_ansible_json_query(
    cmd: list[str],
    limit_to: str = "all",
    jq: list[str] | None = None,
    select: list[str] | None = None,
    drop: list[str] | None = None,
    extract: str | None = None,
    sort: list[str] | None = None,
    sort_reverse: bool = False,
    unique: bool = False,
    **kwargs: Any,
) -> Any:
    return _exec_json_query(
        cmd=["ansible", limit_to, "--one-line"] + cmd,
        jq=jq,
        select=select,
        drop=drop,
        extract=extract,
        sort=sort,
        sort_reverse=sort_reverse,
        unique=unique,
        **kwargs,
    )


def _exec_ansibleinv_json_query(
    jq: list[str] | None = None,
    select: list[str] | None = None,
    drop: list[str] | None = None,
    extract: str | None = None,
    sort: list[str] | None = None,
    sort_reverse: bool = False,
    unique: bool = False,
    **kwargs: Any,
) -> Any:
    return _exec_json_query(
        cmd=["ansible-inventory", "--list"],
        jq=jq,
        select=select,
        drop=drop,
        extract=extract,
        sort=sort,
        sort_reverse=sort_reverse,
        unique=unique,
        **kwargs,
    )


def _exec_ansible_docker_json_query(
    cmd: list[str],
    limit_to: str = SWARM_GROUP_NAME,
    jq: list[str] | None = None,
    select: list[str] | None = None,
    drop: list[str] | None = None,
    extract: str | None = None,
    sort: list[str] | None = None,
    sort_reverse: bool = False,
    unique: bool = False,
    **kwargs: Any,
):
    return _exec_ansible_json_query(
        [
            "-m",
            "command",
            "-a",
            "docker " + " ".join(cmd) + r""" --format {{ '"{{ json . }}"' }}""",
        ],
        limit_to=limit_to,
        jq=jq,
        select=select,
        drop=drop,
        extract=extract,
        sort=sort,
        sort_reverse=sort_reverse,
        unique=unique,
        **kwargs,
    )


def _exec_docker_json_query(
    cmd: list[str],
    jq: list[str] | None = None,
    select: list[str] | None = None,
    drop: list[str] | None = None,
    extract: str | None = None,
    sort: list[str] | None = None,
    sort_reverse: bool = False,
    unique: bool = False,
    **kwargs: Any,
) -> Any:
    return _exec_json_query(
        cmd=["docker", *cmd, "--format", r"{{ json . }}"],
        jq=jq,
        select=select,
        drop=drop,
        extract=extract,
        sort=sort,
        sort_reverse=sort_reverse,
        unique=unique,
        **kwargs,
    )
