import rclpy as rp
from rclpy.node import Node
from turtlesim.msg import Pose
from my_first_package_msgs.msg import CmdAndPoseVel        
from geometry_msgs.msg import Twist                   # import

class CmdAndPose(Node):
  def __init__(self):
    super().__init__('turtle_cmd_pose')
    self.sub_pose = self.create_subscription(Pose, '/turtle1/pose', self.callback_pose, 10)
    self.sub_cmdvel = self.create_subscription(Twist, '/turtle1/cmd_vel', self.callback_cmd, 10)  # 구독 추가
    
    # 추가
    self.publisher = self.create_publisher(CmdAndPoseVel, '/cmd_and_pose', 10)
    self.timer_period = 1.0
    self.timer = self.create_timer(self.timer_period, self.timer_callback)
    self.cmd_pose = CmdAndPoseVel()

  # 추가
  def timer_callback(self): 
    self.publisher.publish(self.cmd_pose)  


  # 전역 설정된(self) 데이터 정의를 이하에서 사용할 것이다
  def callback_pose(self, msg):                             
    self.cmd_pose.pose_x = msg.x              
    self.cmd_pose.pose_y = msg.y              
    self.cmd_pose.linear_vel = msg.linear_velocity
    self.cmd_pose.angular_vel = msg.angular_velocity 

  # 추가: 상단에서 전역으로 인스턴스화한 self.cmd_pose 사용하여 새로운 데이터 정의함
  def callback_cmd(self, msg):
    self.cmd_pose.cmd_vel_linear = msg.linear.x
    self.cmd_pose.cmd.vel_angular = msg.angular.z
    print(self.cmd_pose)


def main(args=None):
  rp.init(args=args)

  turtle_cmd_pose_node = CmdAndPose()
  rp.spin(turtle_cmd_pose_node)

  turtle_cmd_pose_node.destroy_node()
  rp.shutdown()


if __name__ == '__main__':
  main()