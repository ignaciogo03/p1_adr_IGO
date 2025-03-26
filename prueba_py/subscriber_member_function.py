import rclpy
from rclpy.node import Node
from sensor_msgs.msg import NavSatFix

class GPSSubscriber(Node):
    def __init__(self):
        super().__init__('gps_surmanito_escuchando')
        self.subscription = self.create_subscription(
            NavSatFix,
            'gps/fix',
            self.callback,
            10
        )

    def callback(self, msg):
        self.get_logger().info(
            f'Recibido -> Lat: {msg.latitude}, Lon: {msg.longitude}, Alt: {msg.altitude}'
        )

rclpy.init()
node = GPSSubscriber()
rclpy.spin(node)
