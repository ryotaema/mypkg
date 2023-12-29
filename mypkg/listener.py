# SPDX-FileCopyrightText: 2023 Ryota Ema <rhenium4694@gmail.com>
# SPDX-License-Identifier: BSD-3-Clause


import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Listener(Node):
    def __init__(self):
        super().__init__('listen_node')
        self.pub = self.create_subscription(Int16,"countup",self.cb, 10)
    def cb(self,msg):
        self.get_logger().info("Listen: %d " % msg.data)

def main():
    rclpy.init()
    listen = Listener()
    rclpy.spin(listen)
    listen.destory_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
