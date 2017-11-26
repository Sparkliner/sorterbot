#!/usr/bin/env python

import rospy
from sbot_msg.msg import Position2D

def talker():
	pub = rospy.Publisher('targetposition', Position2D, queue_size =10)
	rospy.init_node('talker', anonymous=True)
	rate = rospy.Rate(10)
	outputData = Position2D()
	while not rospy.is_shutdown():
		outputData.x = 1.0
		outputData.y = 2.0
		#rospy.loginfo(outputData)
		pub.publish(outputData)
		rate.sleep()


if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass