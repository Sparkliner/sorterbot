#!/usr/bin/env python
import rospy
from sbot_msg.msg import EFCommand
from sbot_msg.msg import EFStatus

import Adafruit_BBIO.GPIO as GPIO

def shutItDown():
	GPIO.output("P8_10", GPIO.LOW)
	GPIO.cleanup()

def listener():
	rospy.on_shutdown(shutItDown)

	rospy.init_node('pump_gpio_control', anonymous=True)

	#rospy subscribe
	#rospy.spin()

	#test code
	GPIO.setup("P8_10", GPIO.OUT)
	while not rospy.is_shutdown():
		GPIO.output("P8_10", GPIO.HIGH)
		rospy.sleep(5.)
		GPIO.output("P8_10", GPIO.LOW)
		rospy.sleep(5.)


if __name__ == '__main__':
	listener()