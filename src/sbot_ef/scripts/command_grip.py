#!/usr/bin/env python
import rospy
from sbot_msg.msg import EFCommand
from sbot_msg.msg import EFStatus

import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM

OUT_PIN = "P8_10"
IN_PIN = "P8_14"
SERVO_PIN = "P8_13"

SERVOMAX = 180.0
ANGLE_LOWERED = 80.0
ANGLE_RAISED = 0.0
MINPULSE_MS = 0.5
MAXPULSE_MS = 2.5
SERVO_FREQUENCY = 50


MINDUT = MINPULSE_MS*(SERVO_FREQUENCY/1000.0)*100
MAXDUT = MAXPULSE_MS*(SERVO_FREQUENCY/1000.0)*100

def shutItDown():
	#turn pump off
	PWM.start(SERVO_PIN, MINDUT, SERVO_FREQUENCY, 0)
	PWM.stop(SERVO_PIN)
	GPIO.output(OUT_PIN, GPIO.LOW)
	GPIO.cleanup()
	PWM.cleanup()

def commandlistener(cmdmessage):
	GPIO.setup(OUT_PIN, GPIO.OUT)
        GPIO.setup(IN_PIN, GPIO.IN)
	rospy.sleep(2)
        msg = EFStatus()
        msg.status = msg.EF_BUSY
        pub.publish(msg)

	if (cmdmessage.command == cmdmessage.CMD_GRAB):
		#initialize suckage
		GPIO.output(OUT_PIN, GPIO.HIGH)
		#reset servo just in case
		angle = 0.0
		#move in to grab
		while ((not GPIO.input(IN_PIN)) and (angle < ANGLE_LOWERED)):
			dutycyc = MINDUT + (MAXDUT-MINDUT)*(angle/SERVOMAX)
			PWM.start(SERVO_PIN, dutycyc, SERVO_FREQUENCY, 0)
			angle += 5
			rospy.sleep(0.25)
		if GPIO.input(IN_PIN):
			#we have contacted something
			#carefully retract
			while ((angle > ANGLE_RAISED)):
				dutycyc = MINDUT + (MAXDUT-MINDUT)*(angle/SERVOMAX)
				PWM.start(SERVO_PIN, dutycyc, SERVO_FREQUENCY, 0)
				angle -= 5
				rospy.sleep(0.5)
		if not (GPIO.input(IN_PIN)):
			#we dropped it or never got it in the first place
			while ((angle > ANGLE_RAISED)):
				dutycyc = MINDUT + (MAXDUT-MINDUT)*(angle/SERVOMAX)
				PWM.start(SERVO_PIN, dutycyc, SERVO_FREQUENCY, 0)
				angle -= 5
				rospy.sleep(0.5)
			#for now, retract as usual
		#we made it this far, this probably still have it
		msg = EFStatus()
		msg.status = msg.EF_READY
		pub.publish(msg)
	else:
		#kinda like in reverse
		GPIO.output(OUT_PIN, GPIO.LOW) #end suckage
		#reset angle
		angle = 0.0
		dutycyc = MINDUT + (MAXDUT-MINDUT)*(angle/SERVOMAX)
		PWM.start(SERVO_PIN, dutycyc, SERVO_FREQUENCY, 0)
		msg = EFStatus()
		msg.status = msg.EF_READY
		pub.publish(msg)
	
def initialize():
	global pub
	rospy.on_shutdown(shutItDown)
	PWM.start(SERVO_PIN, MINDUT, SERVO_FREQUENCY, 0)
	rospy.init_node('pump_gpio_control', anonymous=True)
	pub = rospy.Publisher('ef_status', EFStatus, queue_size=1000, latch = True)
	#GPIO.setup(OUT_PIN, GPIO.OUT)
        #GPIO.setup(IN_PIN, GPIO.IN)
	#initialize suckage
        #GPIO.output(OUT_PIN, GPIO.HIGH)
        #reset servo just in case
        #angle = 0.0
        #move in to grab
        #while ((not GPIO.input(IN_PIN)) and (angle < ANGLE_LOWERED)):
        #        dutycyc = MINDUT + (MAXDUT-MINDUT)*(angle/SERVOMAX)
        #        PWM.start(SERVO_PIN, dutycyc, SERVO_FREQUENCY, 0)
        #        angle += 5
        #        rospy.sleep(0.25)


	rospy.Subscriber('ef_command', EFCommand, commandlistener)

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

def inputtest():
	rospy.on_shutdown(shutItDown)

	rospy.init_node('pump_gpio_control', anonymous=True)

	GPIO.setup(OUT_PIN, GPIO.OUT)
	GPIO.setup(IN_PIN, GPIO.IN)

	while not rospy.is_shutdown():
		if GPIO.input(IN_PIN):
			rospy.loginfo("Switch closed")
		else:
			rospy.loginfo("Switch open")


if __name__ == '__main__':
	initialize()
