import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class TurtleController(Node):
    def __init__(self):
        super().__init__('turtle_controller')
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.time = 0

    def create_twist(self, linear_x, angular_z):
        msg = Twist()
        msg.linear.x = linear_x
        msg.angular.z = angular_z
        return msg

    def get_twist_msg(self):
        if self.time < 1:
            msg = self.create_twist(0.0,0.0) # sit still for a second, rotation used at first for debugging purposes but now not needed
        elif self.time % 2 == 1 and self.time < 20:
            msg = self.create_twist(3.0, 0.0) # draw straight line
        elif self.time % 2 == 0 and self.time <20:
            msg = self.create_twist(0.0, 3.770) # rotate about 216 degrees, this is what produces the sunflower petals
        else:
            msg = self.create_twist(0.0, 0.0) # stop moving once shape is done being created
        return msg
    
    def timer_callback(self):
        msg = self.get_twist_msg()       
        self.publisher.publish(msg)
        self.time += 1
        print("time: {}".format(self.time))

def main(args=None):
    rclpy.init(args=args)

    turtle_controller = TurtleController()

    rclpy.spin(turtle_controller)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    turtle_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
