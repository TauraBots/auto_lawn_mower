import rospy
from geometry_msgs.msg import Twist
import sys, select, termios, tty

twist = Twist()
rospy.init_node("teste")
pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)


while not rospy.is_shutdown():

	twist.linear.x = 1.8
	twist.linear.y = 0.0
	twist.linear.z = 0.0
        
	twist.angular.x = 1.0
	twist.angular.y = 0.0
	twist.angular.z = 1.0
        
        pub.publish(twist)

