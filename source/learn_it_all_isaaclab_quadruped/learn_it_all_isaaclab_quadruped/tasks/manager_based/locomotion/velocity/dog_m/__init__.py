# Copyright (c) 2022-2025, The Isaac Lab Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

"""Gym registrations for the current custom quadruped task."""

import gymnasium as gym

from . import agents


def _register(task_id: str, env_cfg: str, rsl_cfg: str, skrl_cfg: str) -> None:
    gym.register(
        id=task_id,
        entry_point="isaaclab.envs:ManagerBasedRLEnv",
        disable_env_checker=True,
        kwargs={
            "env_cfg_entry_point": env_cfg,
            "rsl_rl_cfg_entry_point": rsl_cfg,
            "skrl_cfg_entry_point": skrl_cfg,
        },
    )


_register(
    task_id="LearnItAll-DogM-Direct-v0",
    env_cfg=f"{__name__}.flat_env_cfg:DogMFlatEnvCfg",
    rsl_cfg=f"{agents.__name__}.rsl_rl_ppo_cfg:DogMFlatPPORunnerCfg",
    skrl_cfg=f"{agents.__name__}:skrl_flat_ppo_cfg.yaml",
)
_register(
    task_id="LearnItAll-DogM-Flat-v0",
    env_cfg=f"{__name__}.flat_env_cfg:DogMFlatEnvCfg",
    rsl_cfg=f"{agents.__name__}.rsl_rl_ppo_cfg:DogMFlatPPORunnerCfg",
    skrl_cfg=f"{agents.__name__}:skrl_flat_ppo_cfg.yaml",
)
_register(
    task_id="LearnItAll-DogM-Flat-Play-v0",
    env_cfg=f"{__name__}.flat_env_cfg:DogMFlatEnvCfgPlay",
    rsl_cfg=f"{agents.__name__}.rsl_rl_ppo_cfg:DogMFlatPPORunnerCfg",
    skrl_cfg=f"{agents.__name__}:skrl_flat_ppo_cfg.yaml",
)
_register(
    task_id="LearnItAll-DogM-Rough-v0",
    env_cfg=f"{__name__}.rough_env_cfg:DogMRoughEnvCfg",
    rsl_cfg=f"{agents.__name__}.rsl_rl_ppo_cfg:DogMRoughPPORunnerCfg",
    skrl_cfg=f"{agents.__name__}:skrl_rough_ppo_cfg.yaml",
)
_register(
    task_id="LearnItAll-DogM-Rough-Play-v0",
    env_cfg=f"{__name__}.rough_env_cfg:DogMRoughEnvCfgPlay",
    rsl_cfg=f"{agents.__name__}.rsl_rl_ppo_cfg:DogMRoughPPORunnerCfg",
    skrl_cfg=f"{agents.__name__}:skrl_rough_ppo_cfg.yaml",
)
