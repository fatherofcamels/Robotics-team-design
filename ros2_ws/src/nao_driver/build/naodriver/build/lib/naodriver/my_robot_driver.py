import rclpy
from sensor_msgs.msg import Range



class MyRobotDriver:
    def init(self, webots_node, properties):
        self.__robot = webots_node.robot
        self.__timestep = int(self.__robot.getBasicTimeStep())

        # Sensors
        #self.__gps = self.__robot.getDevice()

        rclpy.init(args=None)
        self.__node = rclpy.create_node('my_robot_driver')
        self.__node.create_subscription(Range,'/bob/Sonar/Left')
        


    def step(self):
        rclpy.spin_once(self.__node, timeout_sec=0)