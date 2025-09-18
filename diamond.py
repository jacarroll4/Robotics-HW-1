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
            msg = self.create_twist(0.0,1.571) # rotate 45 degrees to make diamond clearer to see
        elif self.time >= 1 and self.time < 3:
            msg = self.create_twist(1.0, 0.0) # make first line of diamond
        elif self.time >= 3 and self.time < 4:
            msg = self.create_twist(0.0, 2.09) # rotate 120 degrees roughly
        elif self.time >= 4 and self.time < 6:
            msg = self.create_twist(1.0, 0.0) # make second, equal-sized line of diamond
        elif self.time >= 6 and self.time < 7:
            msg = self.create_twist(0.0, 4.101) # rotate roughly 235 degrees
        elif self.time >= 7 and self.time < 9:
            msg = self.create_twist(1.0, 0.0) # make third equal sized line of diamond
        elif self.time >= 9  and self.time < 10:
            msg = self.create_twist(0.0, 2.09) # rotate same 120 degrees roughly to complete 3/4 of diamond
        elif self.time >= 10 and self.time < 12:
            msg = self.create_twist(1.0, 0.0) # draw final line to make diamond 4 equals sides and angles
        else:
            msg = self.create_twist(0.0, 0.0) # stop moving once shape is drawn
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
