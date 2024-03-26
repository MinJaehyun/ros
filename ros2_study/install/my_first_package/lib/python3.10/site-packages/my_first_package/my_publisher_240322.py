import rclpy as rp
from rclpy.node import Node

from geometry_msgs.msg import Twist


# 개념:
# 발행하는 코드이다.
# 뭐를? Twist 타입(데이터 정의) 사용하여,
# turtle 1에 cmd_vel 토픽을 버스를 통해 데이터를 전달한다.
class TurtlesimPublisher(Node):
    def __init__(self):
        super().__init__('turtlesim_publisher')
        self.publisher = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.timer_period = 0.5
        self.timer = self.create_timer(self.timer_period, self.timer_callback, 10)
    
    def timer_callback(self):
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 2.0
        self.publisher.publish(msg)


def main(args=None):
    rp.init(args=args)

    turtlesim_publisher = TurtlesimPublisher()

    rp.spin(turtlesim_publisher)

    turtlesim_publisher.destroy_publisher()
    rp.shutdown()


if __name__ == '__main__':
    main()