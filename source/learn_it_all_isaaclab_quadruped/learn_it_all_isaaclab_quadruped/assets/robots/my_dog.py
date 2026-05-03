# Copyright (c) 2022-2025, The Isaac Lab Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

"""Custom quadruped articulation definitions."""

from __future__ import annotations

import os

import isaaclab.sim as sim_utils
from isaaclab.actuators import DCMotorCfg
from isaaclab.assets.articulation import ArticulationCfg

_ASSET_ROOT = os.path.join(os.path.dirname(__file__), "data")


def _asset_path(*parts: str) -> str:
    return os.path.join(_ASSET_ROOT, *parts)


DOG_M_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=_asset_path("dog2", "dog.usd"),
        activate_contact_sensors=True,
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=False,
            retain_accelerations=False,
            linear_damping=0.0,
            angular_damping=0.0,
            max_linear_velocity=1000.0,
            max_angular_velocity=1000.0,
            max_depenetration_velocity=1.0,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=False,
            solver_position_iteration_count=4,
            solver_velocity_iteration_count=0,
        ),
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.22),
        joint_pos={
            ".*L_hip_joint": 0.1,
            ".*R_hip_joint": -0.1,
            "F[L,R]_thigh_joint": 0.8,
            "R[L,R]_thigh_joint": 1.0,
            ".*_calf_joint": -1.5,
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=0.9,
    actuators={
        "base_legs": DCMotorCfg(
            joint_names_expr=[".*_hip_joint", ".*_thigh_joint", ".*_calf_joint"],
            effort_limit=25,
            saturation_effort=25,
            velocity_limit=21.0,
            stiffness=15.0,
            damping=0.2,
            friction=0.0,
        ),
    },
)


DOG_M_LEGACY_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=_asset_path("dog1", "dog.usd"),
        activate_contact_sensors=True,
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=False,
            retain_accelerations=False,
            linear_damping=0.0,
            angular_damping=0.0,
            max_linear_velocity=1000.0,
            max_angular_velocity=1000.0,
            max_depenetration_velocity=1.0,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=False,
            solver_position_iteration_count=4,
            solver_velocity_iteration_count=0,
        ),
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.2),
        joint_pos={
            "left_front_hip_joint": 0.0,
            "left_front_knee_joint": 0.0,
            "left_front_ankle_joint": 0.0,
            "right_front_hip_joint": 0.0,
            "right_front_knee_joint": 0.0,
            "right_front_ankle_joint": 0.0,
            "left_back_hip_joint": 0.0,
            "left_back_knee_joint": 0.0,
            "left_back_ankle_joint": 0.0,
            "right_back_hip_joint": 0.0,
            "right_back_knee_joint": 0.0,
            "right_back_ankle_joint": 0.0,
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=0.9,
    actuators={
        "base_legs": DCMotorCfg(
            joint_names_expr=[".*_hip_joint", ".*_knee_joint", ".*_ankle_joint"],
            effort_limit=5,
            saturation_effort=5,
            velocity_limit=1.5,
            stiffness=10.0,
            damping=0.01,
            friction=0.0,
        ),
    },
)
