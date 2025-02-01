#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import math

class GoToPoint(Node):
    def __init__(self):
        super().__init__('go_to_point')
        self.pub = self.create_publisher(Twist, 'cmd_vel', 10)
        self.sub = self.create_subscription(Odometry, 'odom', self.odom_callback, 10)
        
        self.target = (0.0, -0.5)
        self.speed = 0.2
        self.tolerance = 0.05
        self.position = (1.0, 1.0)  # Başlangıç konumu farklı bir değer olarak ayarlandı

    def odom_callback(self, msg):
        self.position = (msg.pose.pose.position.x, msg.pose.pose.position.y)
        
        if self.position is not None and self.distance_to_target() > self.tolerance:
            self.move()
        else:
            self.stop()

    def distance_to_target(self):
        if self.position is None:
            return float('inf')  # Konum bilinmiyorsa maksimum mesafe döndür
        return math.dist(self.position, self.target)
    
    def move(self):
        twist = Twist()
        twist.linear.x = self.speed
        self.pub.publish(twist)
    
    def stop(self):
        self.pub.publish(Twist())
        self.get_logger().info('Goal reached!')


def main():
    rclpy.init()
    node = GoToPoint()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

