#!/usr/bin/env python
import rospy
from sbot_msg.msg import EFCommand
from sbot_msg.msg import EFStatus

import Adafruit_BBIO.GPIO as GPIO

OUT_PIN = "P8_10"
IN_PIN = "P8_14"

def shutItDown():
	#turn pump off
	GPIO.output(OUT_PIN, GPIO.LOW)
	GPIO.cleanup()

def grabit():
	pass

def listener():
	rospy.on_shutdown(shutItDown)

	rospy.init_node('pump_gpio_control', anonymous=True)

	#rospy subscribe
	#rospy.spin()

	#test code
	GPIO.setup(OUT_PIN, GPIO.OUT)
	GPIO.setup(IN_PIN, GPIO.IN)

	
	while not rospy.is_shutdown():
		if GPIO.input(IN_PIN)
			rospy.loginfo("INPUT HIGH")
		else
			rospy.loginfo("INPUT LOW")
		# GPIO.output(OUT_PIN, GPIO.HIGH)
		# rospy.sleep(5.)
		# GPIO.output(OUT_PIN, GPIO.LOW)
		# rospy.sleep(5.)


if __name__ == '__main__':
	listener()