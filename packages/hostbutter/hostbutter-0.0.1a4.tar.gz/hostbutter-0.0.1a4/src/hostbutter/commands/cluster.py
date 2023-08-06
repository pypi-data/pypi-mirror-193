from __future__ import annotations

import os
import sys
from typing import Any

import myke
import yapx

from ..query import (
    _exec_ansible_json_query,
    _exec_ansibleinv_json_query,
    _print_results,
)
from ..utils import set_cwd
from .context import context_current

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


def cluster_playbook(
    name: str,
    limit_to: str = "all",
    password_auth: bool = False,
    _ansible_args: list[str] | None = None,
):
    with set_cwd(os.path.dirname(os.environ["ANSIBLE_INVENTORY"])):
        pb_args: list[str] = []
        if password_auth:
            pb_args.append("-kK")
        if _ansible_args:
            pb_args.extend(_ansible_args)
        pb_args.append(name)

        myke.run(["ansible-playbook", "-l", limit_to] + pb_args)


def cluster_setup(
    scope: None
    | Literal["ssh", "dns", "firewall", "swarm", "contexts", "labels"] = yapx.arg(
        None,
        pos=True,
    ),
    limit_to: str = "all",
    password_auth: bool = False,
):
    ansible_args: list[str] | None = None

    playbook: str = "fresh2dev.hostbutter.apply_swarm"

    if scope:
        if scope == "ssh":
            playbook = "fresh2dev.hostbutter.apply_ssh"
        else:
            ansible_args = ["--tag"]
            if scope == "swarm":
                ansible_args.append("swarm")
            elif scope == "contexts":
                ansible_args.append("swarm-contexts")
            elif scope == "labels":
                ansible_args.append("swarm-labels")
            elif scope == "firewall":
                ansible_args.append("firewall")
            elif scope == "dns":
                ansible_args.extend(
                    ["dns", "--skip-tags", "dnsmasq-install-dependencies"],
                )
            else:
                raise ValueError("Unknown scope: " + scope)

    cluster_playbook(
        playbook,
        limit_to=limit_to,
        password_auth=password_auth,
        _ansible_args=ansible_args,
    )


def cluster_create():
    inventory: str = os.environ["ANSIBLE_INVENTORY"]
    if os.path.exists(inventory):
        raise FileExistsError(inventory)
    os.makedirs(os.path.dirname(inventory))
    with open(inventory, "w+", encoding="utf-8") as f:
        domain: str = os.getenv("HB_DOMAIN", "example.com")
        f.write(
            f"""---
all:
  vars:
    domain: {domain}
    ansible_python_interpreter: python3
    ansible_port: 22
    ansible_ssh_private_key_file: "~/.ssh/id_ed25519.pub"
    root_ca_cert: ""
    timesync_timezone: America/Chicago
    fail2ban_install: true
    fail2ban_maxretry: 5     # allow up to 5 ssh failures,
    fail2ban_findtime: 1440  # in a 24-hour span,
    fail2ban_bantime: 10080  # ban for 7 days.
    dnsmasq_dns_servers:
      - 1.1.1.1
      - 1.0.0.1
    # dnsmasq_wildcard_addresses:
    #   "{domain}": "192.168.69.2"
    dnsmasq_host_records:
      "nas.{domain}": "192.168.69.2"
      "git.{domain}": "192.168.69.2"
      "registry.{domain}": "192.168.69.2"
    docker_daemon_options:
      dns: []
      default-address-pools:
        - base: "10.10.0.0/16"
          size: 24
      log-driver: "json-file"
      log-opts:
        max-size: "10m"
        max-file: "5"
      metrics-addr: '0.0.0.0:9323'
      experimental: true
  children:
    docker_swarm:
      children:
        docker_swarm_manager:
          hosts:
            swarm-mgr-01:
              ansible_host: "1.234.456.78"
              ansible_user: user
              docker_swarm_interface: enp7s0
              swarm_labels:
                - proxy
                - nas
                - frontend
                - backend
                - git-server
                - collector
              nfs_exports:
                - "/mnt/data            *(rw,fsid=0,crossmnt,sync,no_subtree_check,no_auth_nlm,insecure,no_root_squash)"
              firewall_additional_rules: []

        docker_swarm_worker:
          hosts: {{}}

    non_swarm: {{}}
""",
        )
    myke.run([os.getenv("EDITOR", "vim"), os.environ["ANSIBLE_INVENTORY"]])


def cluster_edit():
    myke.run([os.getenv("EDITOR", "vim"), os.environ["ANSIBLE_INVENTORY"]])


def cluster_ls():
    myke.echo.lines(
        [
            x
            for x in os.listdir(
                os.path.dirname(os.path.dirname(os.environ["ANSIBLE_INVENTORY"])),
            )
            if not x.startswith(".")
        ],
    )


def cluster_query(
    view: Literal[
        "all",
        "os",
        "vol",
        "volumes",
        "chassis",
        "hw",
        "hardware",
        "ip",
        "ips",
        "interfaces",
        "inv",
        "inventory",
        "ssh",
    ] = yapx.arg(pos=True),
    limit_to: str = "all",
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
) -> Any:
    results: Any = None

    if view == "ssh":
        results = _exec_ansible_json_query(
            [
                "-m",
                "shell",
                "-a",
                # r'echo "{\"$(hostname)\": \"{{ ansible_user}}@{{ ansible_host }}:{{ ansible_port }}\"}"',
                (
                    r'echo "{\"Host\": \"$(hostname)\", \"SSH\": \"ssh://{{'
                    r' ansible_user}}@{{ ansible_host }}:{{ ansible_port }}\"}"'
                ),
            ],
            limit_to=limit_to,
            jq=[r". [] | {Name: .__hostname__} + . | del (.__hostname__)"] + jq,
            select=select,
            drop=drop,
            extract=extract,
            sort=sort,
            sort_reverse=sort_reverse,
            unique=unique,
        )

    elif view in ("inv", "inventory"):
        jq_base: str = (
            r".[] | ._meta.hostvars | to_entries[] | {hostname: .key} + .value"
            r" | {hostname, ansible_host, ansible_user, docker_swarm_interface,"
            r" dnsmasq_dns_servers, swarm_labels}"
        )
        results = _exec_ansibleinv_json_query(
            jq=[jq_base] + jq,
            select=select,
            drop=drop,
            extract=extract,
            sort=sort,
            sort_reverse=sort_reverse,
            unique=unique,
        )
    else:
        gather_subset: list[str] = ["!all"]

        jq_base: str = r".[] | .ansible_facts"

        if view == "all":
            gather_subset = ["all"]
        elif view == "os":
            gather_subset = ["lsb", "processor"]
            jq_base += (
                r" | {"
                r" HostName: .ansible_hostname"
                r", OS: .ansible_lsb.description"
                r", Kernel: .ansible_kernel"
                r", Arch: .ansible_architecture"
                # r', User: .ansible_user_id'
                # r', UID: .ansible_user_uid'
                r", UptimeDays: ((10 * .ansible_uptime_seconds/86400 | round)/10.0)"
                r", Time: .ansible_date_time.time"
                r" }"
            )
        elif view in ("vol", "volumes"):
            gather_subset = ["mounts"]
            jq_base += (
                r" | {HostName: .ansible_hostname,"
                r" VolumeMounts: .ansible_mounts[] | select(.size_total > 0)}"
                r" | {"
                r" HostName"
                r", Device: .VolumeMounts.device"
                r", Mount_Point: .VolumeMounts.mount"
                r", Volume_Type: .VolumeMounts.fstype"
                r", Size_GB: ((10 * (.VolumeMounts.size_total/1024/1024/1024) |"
                r" round)/10.0)"
                r", Use_Percent: ((10 * (100 * (.VolumeMounts.size_total -"
                r" .VolumeMounts.size_available) / .VolumeMounts.size_total) |"
                r" round)/10.0)"
                r" }"
            )
        elif view == "chassis":
            gather_subset = ["hardware"]
            jq_base += (
                r" | {"
                r" HostName: .ansible_hostname"
                r", SystemVendor: .ansible_system_vendor"
                r", SystemModel: .ansible_product_name"
                r", FormFactor: .ansible_form_factor"
                r", BoardName: .ansible_board_name"
                r", BiosVersion: .ansible_bios_version"
                r", BiosDate: .ansible_bios_date"
                r" }"
            )
        elif view in ("hw", "hardware"):
            gather_subset = ["hardware"]
            jq_base += (
                r" | {"
                r" HostName: .ansible_hostname"
                # r', System_Vendor: .ansible_system_vendor'
                r", SystemModel: .ansible_product_name"
                r", CPU: .ansible_processor[2]"
                r", CPUCores: .ansible_processor_cores"
                r", RAMTotalGB: ((10*.ansible_memtotal_mb/1024 | round)/10.0)"
                r", RAMUsePercent: ((10*100*.ansible_memfree_mb/.ansible_memtotal_mb |"
                r" round)/10.0)"
                r" }"
            )
        elif view in ("ip", "ips", "interfaces"):
            gather_subset = ["network", "dns"]
            jq_base += (
                r" | {ansible_facts: ., main_interfaces: ([.ansible_interfaces[] |"
                r' select(. == "lo" or startswith("veth") or startswith("docker") |'
                r' not)] | map("ansible_"+ .))}'
                r" | {hostname: .ansible_facts.ansible_hostname, domain:"
                r" .ansible_facts.ansible_domain, ifc:"
                r" .ansible_facts[.main_interfaces[]], dns:"
                r" .ansible_facts.ansible_dns.nameservers}"
                r" | select(.ifc.ipv4.address != null)"
                r" | {HostName: .hostname, Domain: .domain, Interface: .ifc.device,"
                r" IPv4: .ifc.ipv4.address, IPv6: [.ifc.ipv6[]?.address], MAC:"
                r" .ifc.macaddress, DNS: .dns}"
            )
        else:
            raise ValueError("Unrecognized query view: " + view)

        results = _exec_ansible_json_query(
            [
                "-m",
                "setup",
                "-a",
                "gather_subset=" + ",".join(gather_subset),
            ],
            limit_to=limit_to,
            jq=[jq_base] + jq,
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


def cluster_ssh(
    host: list[str] | None = yapx.arg(None, pos=True, exclusive=True),
    ls: bool = yapx.arg(False, exclusive=True, flags=["-l", "--list"]),
):
    if ls or not host:
        cluster_query(view="ssh", jq=[], _echo=True, no_table=False)
        return

    for h in host:
        if h.endswith(context_current(from_env=True, _echo=False)):
            h = h.split(".", maxsplit=1)[0]

        results: list[str] = cluster_query(
            limit_to=h,
            view="ssh",
            jq=[],
            extract="SSH",
            _echo=False,
        )

        if not results:
            print("Unknown host name. Select from:")
            cluster_query(view="ssh", jq=[], _echo=True, no_table=False)
            break

        assert len(results) == 1

        myke.run(["ssh", results[0]])

    return


def cluster_groups():
    myke.run(["ansible-inventory", "--graph"])


def cluster_ping(limit_to: str = "all", skip_verify: bool = False):
    myke.run(
        [
            "ansible",
            limit_to,
            "-m",
            "ping",
        ],
        env_update={"ANSIBLE_HOST_KEY_CHECKING": "False"} if skip_verify else {},
    )


def cluster_exec(command: str, limit_to: str = "all"):
    myke.run(["ansible", limit_to, "-m", "shell", "-a", command])
