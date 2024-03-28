import rclpy as rp
from rclpy.action import ActionServer                                 # 
from rclpy.node import Node

from my_first_package_msgs.action import DistTurtle


class DistTurtleServer(Node):
  def __init__(self):
    super().__init__('dist_turtle_action_server')  
    # 'dist_turtle'로 액션 이름 지정하면 $ ros2 action list 내에 존재한다   
    self._action_server = ActionServer(                         # 2
      self, DistTurtle, 'dist_turtle', self.execute_callback)   # 3
    
  def execute_callback(self, goal_handle):                      # 4
    goal_handle.succeed()
    result = DistTurtle.Result()                                # 5
    
    return result


def main(args=None):
  rp.init(args=args)
  dist_turtle_action_server = DistTurtleServer()
  rp.spin(dist_turtle_action_server)


if __name__ == '__main__':
  main()