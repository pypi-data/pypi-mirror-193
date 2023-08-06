from __future__ import annotations

import os
from contextlib import contextmanager

import myke


def current_commit_sha() -> str:
    git_commit_sha, _, _ = myke.run(
        ["git", "rev-parse", "--short", "HEAD"],
        capture_output=True,
        echo=False,
    )
    assert git_commit_sha
    return git_commit_sha.strip()


def current_project_name(from_remote: str = "origin") -> str:
    stdout, _, _ = myke.run(
        ["git", "remote", "get-url", from_remote],
        capture_output=True,
        echo=False,
        check=True,
    )

    assert stdout

    proj_grp, proj_name = stdout.strip().split("/")[-2:]
    if proj_name.endswith(".git"):
        proj_name = os.path.splitext(proj_name)[0]
    proj_name = f"{proj_grp}/{proj_name}"

    return proj_name


@contextmanager
def set_cwd(path: str):
    path_og = os.getcwd()
    try:
        os.chdir(path)
        yield
    finally:
        os.chdir(path_og)


@contextmanager
def set_env(**kwargs):
    env_og = os.environ.copy()
    try:
        for k, v in kwargs.items():
            if v is None:
                os.environ.pop(k)
            else:
                os.environ[k] = v

        yield

    finally:
        os.environ.clear()
        os.environ.update(env_og)
