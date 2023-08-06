from __future__ import annotations

SWARM_GROUP_NAME: str = "docker_swarm"

STACK_NAME_VAR: str = "COMPOSE_PROJECT_NAME"

IMAGE_DEPENDENCIES: list[str] = [
    "quay.io/skopeo/stable:v1.9.2",
    "gcr.io/kaniko-project/executor:v1.9.1",
]

CI_IMAGE_DEPENDENCIES: list[str] = IMAGE_DEPENDENCIES + [
    "docker.io/alpine/git:2.36.3",
    "docker.io/docker:20.10.23-dind",
]
