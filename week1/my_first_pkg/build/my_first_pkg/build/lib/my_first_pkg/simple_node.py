import rclpy
from rclpy.node import Node
import os

class SimpleNode(Node):

    def __init__(self):
        super().__init__('simple_node')

        # TASK 1
        # self.get_logger().info('Welcome to Mobile Robotics Lab')

        # TASK 2
        '''
        current_dir = os.path.dirname(os.path.abspath(__file__))
        counter_file = os.path.join(current_dir, 'run_count.txt')

        if not os.path.exists(counter_file):
            with open(counter_file, 'w') as f:
                f.write('0')

        with open(counter_file, 'r') as f:
            count = int(f.read().strip())

        count += 1

        with open(counter_file, 'w') as f:
            f.write(str(count))

        self.get_logger().info(f'Run count: {count}')
        '''

        # TASK 3 (ACTIVE)
        self.declare_parameter('student_name', '')
        name = self.get_parameter('student_name').value

        if name != "":
            self.get_logger().info(f'Student Name: {name}')
        else:
            self.get_logger().info('student_name not set')


def main(args=None):
    rclpy.init(args=args)

    node = SimpleNode()
    rclpy.spin_once(node, timeout_sec=0.1)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
