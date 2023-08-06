from __future__ import annotations

from typing import Any

import myke
import yapx

from ..constants import SWARM_GROUP_NAME
from ..query import (
    _exec_ansible_docker_json_query,
    _exec_docker_json_query,
    _exec_json_query,
    _print_results,
)
from .cluster import cluster_exec, cluster_ping, cluster_playbook
from .context import context_current, context_ls


def swarm_ssh(
    name: str | None = yapx.arg(None, pos=True),
    dry_run: bool = False,
    _echo: bool = True,
) -> str:
    ctx: str = context_current(from_env=True, _echo=False)
    if not name:
        name = ctx
    elif "." not in name and "." in ctx:
        name += "." + ctx

    matches: list[str] = context_ls(
        jq=[f'.[] | select (.Name == "{name}")'],
        no_table=True,
        _echo=False,
        extract="DockerEndpoint",
    )

    if not matches:
        print("Not a recognized context. Select one of:")
        context_ls(jq=[], no_table=False)
        raise ValueError(name)

    ssh_target: str = matches[0]

    if _echo:
        print(ssh_target)

    if not dry_run:
        myke.run(["ssh", ssh_target])

    return ssh_target


def swarm_exec(command: str):
    cluster_exec(command=command, limit_to=SWARM_GROUP_NAME)


def swarm_query(
    command: list[str] = yapx.arg(pos=True),
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
) -> list[dict[str, Any] | Any]:
    results: Any = _exec_docker_json_query(
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


def swarm_nodes(
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
    # ID: .ID
    # , vCPUs: .Description.Resources.NanoCPUs
    # , MemGB: .Description.Resources.MemoryBytes
    # , MgrAddr: .ManagerStatus.Addr
    # , Labels: .Spec.Labels
    jq.insert(
        0,
        r""".[] | {
    HostName: .Description.Hostname
    , Engine: .Description.Engine.EngineVersion
    , Arch: .Description.Platform.Architecture
    , Role: .Spec.Role
    , Availability: .Spec.Availability
    , State: .Status.State
    , IP: .Status.Addr
    , MgrReachability: .ManagerStatus.Reachability
    , MgrLeader: .ManagerStatus.Leader
}""",
    )

    results = _exec_json_query(
        cmd="docker node ls -q | xargs -n1 docker node inspect --format "
        + r"'{{ json . }}'",
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


def swarm_labels(
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
    # ID: .ID
    # , vCPUs: .Description.Resources.NanoCPUs
    # , MemGB: .Description.Resources.MemoryBytes
    # , MgrAddr: .ManagerStatus.Addr
    jq.insert(
        0,
        (
            r".[] | [.Spec.Labels | to_entries"
            r" | map({Label: .key, Value: .value})][][] + {Node: .Description.Hostname}"
        ),
    )

    results = _exec_json_query(
        cmd="docker node ls -q | xargs -n1 docker node inspect --format "
        + r"'{{ json . }}'",
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


def swarm_networks(
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
            r".[] | {Name: .Name, Subnet: .IPAM.Config[]?.Subnet, Containers:"
            r" .Containers | length, Peers: .Peers | length, Scope: .Scope, Driver:"
            r" .Driver, Internal: .Internal, Ingress: .Ingress, Attachable:"
            r" .Attachable}"
        ),
    )

    results = _exec_json_query(
        cmd=(
            r"docker network ls --format '{{ .Name }}'"
            r" | xargs -n1 docker network inspect --format '{{ json . }}'"
        ),
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


def swarm_ping():
    cluster_ping(limit_to=SWARM_GROUP_NAME)


def swarm_prune():
    swarm_exec(
        command=(
            'docker system prune --all --volumes --force && (for x in "volume"; do'
            " docker $x rm $(docker $x ls -q) 2>/dev/null || true; done)"
        ),
    )


def swarm_stats(
    verbose: bool = False,
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
):
    jq_base: str = (
        r".[] | {"
        r" HostName: .__hostname__"
        r", Task: .Name"
        r", Container"
        r", CPUPerc: (.CPUPerc[:-1] | tonumber)"
        r", MemPerc: (.MemPerc[:-1] | tonumber)"
        r", MemUsage"
        r", ID, BlockIO, NetIO, PIDs"
        r"}"
    )

    if not verbose:
        jq_base += r" | del(.ID, .BlockIO, .NetIO, .PIDs)"

    jq = ([jq_base] + jq) if jq else [jq_base]

    results = _exec_ansible_docker_json_query(
        ["stats", "--no-stream"],
        limit_to=SWARM_GROUP_NAME,
        jq=jq,
        select=select,
        drop=drop,
        extract=extract,
        sort=sort,
        sort_reverse=sort_reverse,
        unique=unique,
    )

    if extract:
        raw = True
    _print_results(results, no_table=no_table, pretty=pretty, raw=raw)


def swarm_reboot():
    cluster_playbook("fresh2dev.hostbutter.reboot_swarm", limit_to=SWARM_GROUP_NAME)
