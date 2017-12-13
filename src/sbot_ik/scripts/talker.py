#!/usr/bin/env python

import rospy
from sbot_msg.msg import Position2D

def talker():
	pub = rospy.Publisher('targetposition', Position2D, queue_size =10)
	rospy.init_node('talker', anonymous=True)
	rate = rospy.Rate(1)
	outputData = Position2D()
	myX = -23
	myY = 23
	while not rospy.is_shutdown():
		outputData.x = myX
		outputData.y = myY

		myX = myX+1
		if (myX > 23):
			myX = -23
			myY = myY + 2
			if (myY > 54):
			myY = 23

		#rospy.loginfo(outputData)
		pub.publish(outputData)
		rate.sleep()

	# outputData.x = myX
	# outputData.y = myY

	# pub.publish(outputData)


if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass