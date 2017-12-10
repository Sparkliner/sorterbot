#!/usr/bin/env python
import rospy
from sbot_msg.msg import EFCommand
from sbot_msg.msg import EFStatus

import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM

OUT_PIN = "P8_10"
IN_PIN = "P8_14"
SERVO_PIN = "P8_13"

SERVOMAX = 180
ANGLE_LOWERED = 90
ANGLE_RAISED = 30
MINPULSE_MS = 0.5
MAXPULSE_MS = 2.5
SERVO_FREQUENCY = 50


MINDUT = MINPULSE_MS*(SERVO_FREQUENCY/1000.0)*100
MAXDUT = MAXPULSE_MS*(SERVO_FREQUENCY/1000.0)*100

def shutItDown():
	#turn pump off
	GPIO.output(OUT_PIN, GPIO.LOW)
	GPIO.cleanup()

def initialize(cmdmessage):
	if (cmdmessage.command == cmdmessage.CMD_GRAB):
		#reset servo just in case
		angle = 0;
		#move in to grab
		while ((not GPIO.input(IN_PIN)) and (angle < ANGLE_LOWERED)):
			dutycyc = MINDUT + (MAXDUT-MINDUT)*(angle/JOINT1MAX)
			PWM.start(SERVO_PIN, dutycyc, SERVO_FREQUENCY, 0)
			angle += 5
			rospy.sleep(0.25)
		if GPIO.input(IN_PIN):
			#we have contacted something, turn on vacuum
			GPIO.output(OUT_PIN, GPIO.HIGH)
			#carefully retract
			while ((GPIO.input(IN_PIN)) and (angle > ANGLE_RAISED)):
				dutycyc = MINDUT + (MAXDUT-MINDUT)*(angle/JOINT1MAX)
				PWM.start(SERVO_PIN, dutycyc, SERVO_FREQUENCY, 0)
				angle -= 5
				rospy.sleep(0.5)
		if not (GPIO.input(IN_PIN)):
			#we dropped it or never got it in the first place
			pass
			#do nothing else for now
		else:
			#we made it this far, this probably still have it
			pub = rospy.Publisher('ef_status', EFStatus, queue_size =10)
			msg = EFStatus()
			msg.status = msg.EF_READY
			pub.publish(msg)
	else if (cmdmessage.command == cmdmessage.CMD_DROP):
		#kinda like in reverse
		GPIO.output(OUT_PIN, GPIO.LOW) #but not really, we just drop it
	else:
		#uh, this shouldn't happen
		pass



def grabit():
	pass

def initialize():
	rospy.on_shutdown(shutItDown)

	rospy.init_node('pump_gpio_control', anonymous=True)

	GPIO.setup(OUT_PIN, GPIO.OUT)
	GPIO.setup(IN_PIN, GPIO.IN)

	rospy.Subscriber("ef_command", EFCommand, commandlistener)

	rospy.spin()
	#test code
	

	
	# while not rospy.is_shutdown():
	# 	if GPIO.input(IN_PIN):
	# 		rospy.loginfo("INPUT HIGH")
	# 	else:
	# 		rospy.loginfo("INPUT LOW")
		# GPIO.output(OUT_PIN, GPIO.HIGH)
		# rospy.sleep(5.)
		# GPIO.output(OUT_PIN, GPIO.LOW)
		# rospy.sleep(5.)


if __name__ == '__main__':
	initialize()
