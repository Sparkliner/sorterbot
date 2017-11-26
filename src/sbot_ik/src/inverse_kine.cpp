#include "ros/ros.h"
#include "sbot_msg/Position2D.h"
#include <math.h>

#define PI 3.1414926535897932

#define L1 25.4
#define L2 25.4

#define ERR 10

double wrapAngle(double angle) // constrain to 0-360
{
	angle = fmod(angle,360);
	if (angle < 0)
	{
		angle += 360;
	}

	return angle;
}

void calculateInverseKinematics(const sbot_msg::Position2D::ConstPtr& loc)
{
	double x, y, angle1, angle2;
	ROS_INFO("Received: x=%f, y=%f", loc->x, loc->y);
	
	x = double(loc->x);
	y = double(loc->y);

	// law of cosines
	angle2 = acos((pow(x,2)+pow(y,2)-pow(L1,2)-pow(L2,2))/(2*L1*L2));
	angle1 = atan2(-L2*sin(angle2)*x+(L1+L2*cos(angle2))*y,(L1+L2*cos(angle2))*x+L2*sin(angle2)*y);

	//convert to degrees and wrap to 0-360
	angle1 = wrapAngle(angle1*180.0/PI);
	angle2 = wrapAngle(angle2*180.0/PI);
	

	if (sqrt(pow(x,2)+pow(y,2)) > (L1+L2)) //test for out of reach conditions
	{
		angle1 = 90;
		angle2 = 90;
	}


	//avoid singularity conditions by using offset ERR
	if (abs(angle2-180.0) < ERR)
	{
		angle2 = 180.0 - ERR;
	}

	if (abs(angle2) < ERR)
	{
		angle2 = ERR;
	}

	
	ROS_INFO("Sending: theta1=%f degres, theta2=%f degrees", angle1, angle2);

	

}

int main(int argc, char **argv)
{
	ros::init(argc,argv,"inverse_kine");
	
	ros::NodeHandle n;
	
	ros::Subscriber sub = n.subscribe("targetposition", 1000, calculateInverseKinematics);
	
	ros::spin();
	
	return 0;
}