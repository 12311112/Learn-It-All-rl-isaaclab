# Copyright (c) 2026, Learn-It-All-IsaacLab-Quadruped contributors.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

"""Custom quadruped external project for Isaac Lab."""

import os

import toml

LEARN_IT_ALL_EXT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))
LEARN_IT_ALL_METADATA = toml.load(os.path.join(LEARN_IT_ALL_EXT_DIR, "config", "extension.toml"))

__version__ = LEARN_IT_ALL_METADATA["package"]["version"]

from . import tasks  # noqa: F401,E402
