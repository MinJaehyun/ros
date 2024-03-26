import rclpy as rp
from rclpy.node import Node
from turtlesim.msg import Pose
from my_first_package_msgs.msg import CmdAndPoseVel         # 데이터 정의 가져오고


class CmdAndPose(Node):
  def __init__(self):
    super().__init__('turtle_cmd_pose')
    self.sub_pose = self.create_subscription(Pose, '/turtle1/pose', self.callback_pose, 10)
    self.cmd_pose = CmdAndPoseVel()            # 새로운 데이터 정의를 하기 위한 인스턴스화

  # 전역 설정된(self) 데이터 정의를 이하에서 사용할 것이다
  def callback_pose(self, msg):                             
    self.cmd_pose.pose_x = msg.x               # pose의 요소를 새로 만든 데이터 정의에 담는다 
    self.cmd_pose.pose_y = msg.y                      # 이하 동
    self.cmd_pose.linear_vel = msg.linear_velocity    # 이하 동
    self.cmd_pose.angular_vel = msg.angular_velocity  # 이하 동 
    print(self.cmd_pose)


def main(args=None):
  rp.init(args=args)

  turtle_cmd_pose_node = CmdAndPose()
  rp.spin(turtle_cmd_pose_node)

  turtle_cmd_pose_node.destroy_node()
  rp.shutdown()


if __name__ == '__main__':
  main()