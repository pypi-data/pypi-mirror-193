from typing import List, Pattern

import mocx
from _pytest.capture import CaptureFixture, CaptureResult

from hostbutter.__main__ import main
from hostbutter.__main__ import sys as target_sys


def test_main_version(capsys: CaptureFixture, version_regex: Pattern):
    # 1. ARRANGE
    args: List[str] = ["version"]

    # 2. ACT
    with mocx.patch.object(target_sys, "argv", [""] + args):
        main()

    # 3. ASSERT
    captured: CaptureResult = capsys.readouterr()
    assert not captured.err
    assert captured.out
    assert version_regex.search(captured.out), "invalid version"


# def test_tmp(capsys: CaptureFixture):
#     # 1. ARRANGE
#     # args: List[str] = ["image-tags", "docker.io/python:latest", "--filter", "3.10.[0-9]*-*"]
#     args: List[str] = ["-c", "default", "registry-ls"]
#     # args: List[str] = ["registry-images", "registry.lokalhost.net"]
#     # args: List[str] = ["image-inspect", "docker.io/python:3.10.8"]

#     # 2. ACT
#     with mocx.patch.object(target_sys, "argv", [""] + args):
#         main()

#     # 3. ASSERT
#     captured: CaptureResult = capsys.readouterr()
#     assert not captured.err
#     assert captured.out
