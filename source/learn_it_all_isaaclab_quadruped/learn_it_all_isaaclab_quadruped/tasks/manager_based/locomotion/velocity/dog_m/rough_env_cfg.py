# Copyright (c) 2022-2025, The Isaac Lab Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

import math

from isaaclab.utils import configclass

from isaaclab_tasks.manager_based.locomotion.velocity.velocity_env_cfg import LocomotionVelocityRoughEnvCfg

from learn_it_all_isaaclab_quadruped.assets.robots import DOG_M_CFG


@configclass
class DogMRoughEnvCfg(LocomotionVelocityRoughEnvCfg):
    def __post_init__(self):
        super().__post_init__()

        self.scene.robot = DOG_M_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot")
        self.scene.height_scanner.prim_path = "{ENV_REGEX_NS}/Robot/trunk"

        self.scene.terrain.terrain_generator.sub_terrains["boxes"].grid_height_range = (0.01, 0.05)
        self.scene.terrain.terrain_generator.sub_terrains["boxes"].grid_width = 0.35
        self.scene.terrain.terrain_generator.sub_terrains["random_rough"].noise_range = (0.01, 0.05)
        self.scene.terrain.terrain_generator.sub_terrains["random_rough"].noise_step = 0.01
        self.scene.terrain.terrain_generator.sub_terrains["pyramid_stairs"].step_height_range = (0.01, 0.05)
        self.scene.terrain.terrain_generator.sub_terrains["pyramid_stairs"].step_width = 0.18
        self.scene.terrain.terrain_generator.sub_terrains["pyramid_stairs_inv"].step_height_range = (0.01, 0.05)
        self.scene.terrain.terrain_generator.sub_terrains["pyramid_stairs_inv"].step_width = 0.18

        self.actions.joint_pos.scale = 0.25

        self.events.push_robot = None
        self.events.add_base_mass.params["mass_distribution_params"] = (0.0, 0.0)
        self.events.add_base_mass.params["asset_cfg"].body_names = "trunk"
        self.events.base_external_force_torque.params["asset_cfg"].body_names = "trunk"
        self.events.reset_robot_joints.params["position_range"] = (0.0, 0.0)
        self.events.reset_base.params = {
            "pose_range": {"x": (-0.5, 0.5), "y": (-0.5, 0.5), "yaw": (-3.14, 3.14)},
            "velocity_range": {
                "x": (0.0, 0.0),
                "y": (0.0, 0.0),
                "z": (0.0, 0.0),
                "roll": (0.0, 0.0),
                "pitch": (0.0, 0.0),
                "yaw": (0.0, 0.0),
            },
        }

        self.rewards.feet_air_time.params["sensor_cfg"].body_names = ".*_foot"
        self.rewards.feet_air_time.weight = 0.50
        self.rewards.undesired_contacts.params["sensor_cfg"].body_names = ".*_calf"
        self.rewards.undesired_contacts.weight = -10.0
        self.rewards.track_lin_vel_xy_exp.weight = 1.5 * 50
        self.rewards.track_lin_vel_xy_exp.params["std"] = math.sqrt(0.25)
        self.rewards.track_ang_vel_z_exp.weight = 0.75 * 50
        self.rewards.track_ang_vel_z_exp.params["std"] = math.sqrt(0.25)
        self.rewards.dof_torques_l2.weight = -1.0e-7
        self.rewards.dof_acc_l2.weight = -2.5e-8
        self.rewards.action_rate_l2.weight = -0.001
        self.rewards.lin_vel_z_l2.weight = -0.02

        self.terminations.base_contact.params["sensor_cfg"].body_names = "trunk"


@configclass
class DogMRoughEnvCfgPlay(DogMRoughEnvCfg):
    def __post_init__(self):
        super().__post_init__()

        self.scene.num_envs = 50
        self.scene.env_spacing = 2.5
        self.scene.terrain.max_init_terrain_level = None
        if self.scene.terrain.terrain_generator is not None:
            self.scene.terrain.terrain_generator.num_rows = 5
            self.scene.terrain.terrain_generator.num_cols = 5
            self.scene.terrain.terrain_generator.curriculum = False

        self.observations.policy.enable_corruption = False
        self.events.base_external_force_torque = None
        self.events.push_robot = None
