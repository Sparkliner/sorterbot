#!/usr/bin/env python
import rospy
from sbot_msg.msg import JointTarget
import Adafruit_BBIO.PWM as PWM

JOINT1MAX = 270
JOINT2MAX = 270
MINPULSE_MS = 0.5
MAXPULSE_MS = 2.5
SERVO_FREQUENCY = 50


MINDUT = MINPULSE_MS*(SERVO_FREQUENCY/1000.0)*100
MAXDUT = MAXPULSE_MS*(SERVO_FREQUENCY/1000.0)*100

def sendArmCommand(jtarget):
	angle1 = jtarget.joint1
	angle2 = jtarget.joint2
	rospy.loginfo("Received angle1 =%f, angle2 =%f",angle1,angle2)
	#calculate the proper duty cycle here
	dutycyc1 = MINDUT + (MAXDUT-MINDUT)*(angle1/JOINT1MAX) #2.5 to 12.5
	dutycyc2 = MINDUT + (MAXDUT-MINDUT)*(angle2/JOINT2MAX) #test different duty cycles
	#PWM.start("PIN",dutycycle,frequency,polarity(1 is inverted))
	PWM.start("P9_14", dutycyc1, SERVO_FREQUENCY, 0) #joint 1
	PWM.start("P9_16", dutycyc2, SERVO_FREQUENCY, 0) #joint 2

def shutItDown():
	#shutdown channels and cleanup
	PWM.stop("P9_14")
	PWM.stop("P9_16")
	PWM.cleanup()

def listener():
	rospy.on_shutdown(shutItDown)

	rospy.init_node('joint_target_listener', anonymous=True)
	rospy.Subscriber("servo_angle_target", JointTarget, sendArmCommand)

	rospy.spin()

if __name__ == '__main__':
	listener()
