#include "ros/ros.h"
#include "sbot_msg/Position2D.h"
#include <math.h>

#define PI 3.1414926535897932

void calculateInverseKinematics(const sbot_msg::Position2D::ConstPtr& loc)
{
	ROS_INFO("Received: x=%f, y=%f", loc->x, loc->y);
}

int main(int argc, char **argv)
{
	ros::init(argc,argv,"inverse_kine");
	
	ros::NodeHandle n;
	
	ros::Subscriber sub = n.subscribe("targetposition", 1000, calculateInverseKinematics);
	
	ros::spin;
	
	return 0;
}