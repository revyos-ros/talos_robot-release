# Copyright (c) 2024 PAL Robotics S.L. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import os
from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from controller_manager.launch_utils import generate_load_controller_launch_description
from launch_pal.include_utils import include_launch_py_description


def generate_launch_description():

    pkg_share_folder = os.path.join(
        get_package_share_directory('talos_controller_configuration'), 'config')

    # Joint state controller
    joint_state_broadcaster_launch = generate_load_controller_launch_description(
        controller_name='joint_state_broadcaster',
        controller_params_file=os.path.join(
            pkg_share_folder, 'joint_state_broadcaster.yaml')
    )

    # Force-torque sensors controller for the wrists
    wrist_left_ft_broadcaster_launch = generate_load_controller_launch_description(
        controller_name='wrist_left_ft_broadcaster',
        controller_params_file=os.path.join(
            pkg_share_folder,
            'wrist_left_ft_broadcaster.yaml'))

    wrist_right_ft_broadcaster_launch = generate_load_controller_launch_description(
        controller_name='wrist_right_ft_broadcaster',
        controller_params_file=os.path.join(
            pkg_share_folder,
            'wrist_right_ft_broadcaster.yaml'))

    # Force-torque sensors controller for the ankles
    ankle_left_ft_broadcaster_launch = generate_load_controller_launch_description(
        controller_name='ankle_left_ft_broadcaster',
        controller_params_file=os.path.join(
            pkg_share_folder,
            'ankle_left_ft_broadcaster.yaml'))

    ankle_right_ft_broadcaster_launch = generate_load_controller_launch_description(
        controller_name='ankle_right_ft_broadcaster',
        controller_params_file=os.path.join(
            pkg_share_folder,
            'ankle_right_ft_broadcaster.yaml'))

    # IMU sensors controller
    imu_sensor_broadcaster_launch = generate_load_controller_launch_description(
        controller_name='imu_sensor_broadcaster',
        controller_params_file=os.path.join(
            pkg_share_folder,
            'imu_sensor_broadcaster.yaml'))

    ld = LaunchDescription()

    ld.add_action(joint_state_broadcaster_launch)
    ld.add_action(wrist_left_ft_broadcaster_launch)
    ld.add_action(wrist_right_ft_broadcaster_launch)
    ld.add_action(ankle_left_ft_broadcaster_launch)
    ld.add_action(ankle_right_ft_broadcaster_launch)
    ld.add_action(imu_sensor_broadcaster_launch)

    return ld
