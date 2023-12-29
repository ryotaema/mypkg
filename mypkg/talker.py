# SPDX-FileCopyrightText: 2023 Ryota Ema <rhenium4694@gmail.com>
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Talker(Node):

    def __init__(self):

        super().__init__('talk_node')
        self.pub = self.create_publisher(Int16,"countup",10)
        self.n = 0
        self.create_timer(0.5,self.cb)

    def cb(self):
        msg = Int16()
        msg.data = self.n
        self.pub.publish(msg)
        key = input("<<")
        if key == 'f':
            self.n += 1
        elif key == 'j':
            self.n -= 1
        else:
            self.n += 0

        #self.get_logger().info("talker: $f" %self.msg)

def main(args=None):
    rclpy.init(args=args)
    talk = Talker()
    rclpy.spin(talk)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
