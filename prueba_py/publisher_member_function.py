# Copyright 2016 Open Source Robotics Foundation, Inc.
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

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import NavSatFix

class GPSPublisher(Node):
    def __init__(self):
        super().__init__('gps_surmanito_publicando')
        self.publisher = self.create_publisher(NavSatFix, 'gps/fix', 10)
        self.timer = self.create_timer(1.0, self.publish_gps)

    def publish_gps(self):
        msg = NavSatFix()
        msg.latitude = 40.4168      # Ejemplo: Madrid
        msg.longitude = -3.7038
        msg.altitude = 667.0

        # Campos obligatorios para evitar warnings
        msg.position_covariance_type = NavSatFix.COVARIANCE_TYPE_UNKNOWN
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = "gps_link"

        self.publisher.publish(msg)
        self.get_logger().info(
            f'Publicando -> Lat: {msg.latitude}, Lon: {msg.longitude}, Alt: {msg.altitude}'
        )

rclpy.init()
node = GPSPublisher()
rclpy.spin(node)
