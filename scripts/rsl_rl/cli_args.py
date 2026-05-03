# Copyright (c) 2022-2025, The Isaac Lab Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

from __future__ import annotations

import argparse
import random
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from isaaclab_rl.rsl_rl import RslRlOnPolicyRunnerCfg


def add_rsl_rl_args(parser: argparse.ArgumentParser):
    """Add RSL-RL arguments to the parser."""
    arg_group = parser.add_argument_group("rsl_rl", description="Arguments for the RSL-RL agent.")
    arg_group.add_argument(
        "--experiment_name",
        type=str,
        default=None,
        help="Name of the experiment folder where logs will be stored.",
    )
    arg_group.add_argument("--run_name", type=str, default=None, help="Run name suffix for the log directory.")
    arg_group.add_argument("--resume", action="store_true", default=False, help="Resume from a checkpoint.")
    arg_group.add_argument("--load_run", type=str, default=None, help="Run folder to resume from.")
    arg_group.add_argument("--checkpoint", type=str, default=None, help="Checkpoint file to resume from.")
    arg_group.add_argument(
        "--logger",
        type=str,
        default=None,
        choices={"wandb", "tensorboard", "neptune"},
        help="Logger backend to use.",
    )
    arg_group.add_argument(
        "--log_project_name",
        type=str,
        default=None,
        help="Project name for wandb or neptune logging.",
    )


def parse_rsl_rl_cfg(task_name: str, args_cli: argparse.Namespace) -> RslRlOnPolicyRunnerCfg:
    """Load and update the RSL-RL config from the gym registry."""
    from isaaclab_tasks.utils.parse_cfg import load_cfg_from_registry

    rsl_rl_cfg: RslRlOnPolicyRunnerCfg = load_cfg_from_registry(task_name, "rsl_rl_cfg_entry_point")
    return update_rsl_rl_cfg(rsl_rl_cfg, args_cli)


def update_rsl_rl_cfg(agent_cfg: RslRlOnPolicyRunnerCfg, args_cli: argparse.Namespace):
    """Update the RSL-RL config using CLI overrides."""
    if hasattr(args_cli, "seed") and args_cli.seed is not None:
        if args_cli.seed == -1:
            args_cli.seed = random.randint(0, 10000)
        agent_cfg.seed = args_cli.seed
    if args_cli.resume is not None:
        agent_cfg.resume = args_cli.resume
    if args_cli.load_run is not None:
        agent_cfg.load_run = args_cli.load_run
    if args_cli.checkpoint is not None:
        agent_cfg.load_checkpoint = args_cli.checkpoint
    if args_cli.run_name is not None:
        agent_cfg.run_name = args_cli.run_name
    if args_cli.logger is not None:
        agent_cfg.logger = args_cli.logger
    if agent_cfg.logger in {"wandb", "neptune"} and args_cli.log_project_name:
        agent_cfg.wandb_project = args_cli.log_project_name
        agent_cfg.neptune_project = args_cli.log_project_name
    if args_cli.experiment_name is not None:
        agent_cfg.experiment_name = args_cli.experiment_name

    return agent_cfg
