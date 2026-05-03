# Copyright (c) 2026, Learn-It-All-IsaacLab-Quadruped contributors.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

"""Installation script for the external quadruped package."""

import os

import toml
from setuptools import find_packages, setup

EXTENSION_PATH = os.path.dirname(os.path.realpath(__file__))
EXTENSION_TOML_DATA = toml.load(os.path.join(EXTENSION_PATH, "config", "extension.toml"))

INSTALL_REQUIRES = [
    "numpy",
    "torch==2.5.1",
    "torchvision>=0.14.1",
    "protobuf>=3.20.2, < 5.0.0",
    "tensorboard",
]

PYTORCH_INDEX_URL = ["https://download.pytorch.org/whl/cu118"]

setup(
    name="learn_it_all_isaaclab_quadruped",
    author=EXTENSION_TOML_DATA["package"]["author"],
    maintainer=EXTENSION_TOML_DATA["package"]["maintainer"],
    url=EXTENSION_TOML_DATA["package"]["repository"],
    version=EXTENSION_TOML_DATA["package"]["version"],
    description=EXTENSION_TOML_DATA["package"]["description"],
    keywords=EXTENSION_TOML_DATA["package"]["keywords"],
    python_requires=">=3.10",
    install_requires=INSTALL_REQUIRES,
    dependency_links=PYTORCH_INDEX_URL,
    include_package_data=True,
    packages=find_packages(),
    package_data={
        "learn_it_all_isaaclab_quadruped": [
            "assets/robots/data/dog1/*",
            "assets/robots/data/dog1/**/*",
            "assets/robots/data/dog2/*",
            "assets/robots/data/dog2/**/*",
            "tasks/**/*.yaml",
        ]
    },
    classifiers=[
        "Natural Language :: English",
        "Programming Language :: Python :: 3.10",
        "Isaac Sim :: 4.5.0",
    ],
    zip_safe=False,
)
