#!/usr/bin/env python
import rospy
from sbot_msg.msg import JointTarget
import Adafruit_BBIO.PWM as PWM

def sendArmCommand(jtarget):
	angle1 = jtarget.joint1
	angle2 = jtarget.joint2
	rospy.loginfo("Received angle1 =%f, angle2 =%f",angle1,angle2)
	#calculate the proper duty cycle here
	dutycyc1 = 5 #0 to 100
	dutycyc2 = 5 #test different duty cycles
	#PWM.start("PIN",dutycycle,frequency,polarity(2 is inverted))
	PWM.start("P9_14", dutycyc1, 50, 0) #joint 1
	PWM.start("P9_16", dutycyc2, 50, 0) #joint 2

def listener():
	rospy.init_node('joint_target_listener', anonymous=True)
	rospy.Subscriber("servo_angle_target", JointTarget, sendArmCommand)

	rospy.spin()

	#shutdown channels and cleanup
	PWM.stop("P9_14")
	PWM.stop("P9_16")
	PWM.cleanup()

if __name__ == '__main__':
	listener()
