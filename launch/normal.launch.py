# Copyright 2024 ShotaAk
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

import launch

from launch_ros.actions import Node


def generate_launch_description():
    talker = Node(package='cpp_pubsub_gdb',
                  executable='talker',
                  output='screen')

    listener = Node(package='cpp_pubsub_gdb',
                    executable='listener',
                    output='screen')

    ld = launch.LaunchDescription()
    ld.add_action(talker)
    ld.add_action(listener)

    return ld
