import rclpy as rp
from rclpy.node import Node

from turtlesim.msg import Pose

class TurtlesimSubscriber(Node):                    # Node를 상속한다
  def __init__(self):
    super().__init__('turtlesim_subscriber')        # 던드 init 사용 시, 노드 클래스는 초기화하기 위해 노드 이름 설정해야 한다. 
    self.subscription = self.create_subscription(Pose, 'turtle1/pose', self.callback, 10)
    self.subscription 

  def callback(self, msg):
    print("X: ", msg.xm, ", Y: ", msg.y)


def main(args=None):
  rp.init(args=args)

  turtlesim_subscriber = TurtlesimSubSciber()       # 인스턴스화(객체화)
  rp.spin(turtlesim_subscriber)
 
  turtlesim_subscriber.destroy_node()
  rp.shutdown()


if __name__ == '__main__':                         # 제일 먼저 실행되는 코드
  main()