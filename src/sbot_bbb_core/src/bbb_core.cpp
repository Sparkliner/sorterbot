#include "ros/ros.h"
#include "sbot_msg/Position2D.h"
#include "sbot_msg/EFCommand.h"
#include "sbot_msg/EFStatus.h"
#include "sbot_msg/TargetColor.h"
#include "sbot_msg/SBotStatus.h"
#include <string>

#include "sbot_bbb_core/color_sort.h"


class SorterBotBBBCore
{

enum SysState {
	READY, RETRIEVAL, DELIVERY
};

struct position{
	double x;
	double y;
};

private:
	SysState SBState;
	position grabposition;
	position dropposition;

	ros::NodeHandle n;
	ros::Publisher PositionPub;
	ros::Publisher EFCommandPub;
	ros::Subscriber ColorSub;
	ros::Subscriber EFStatusSub;
	ros::Subscriber IPSub;

	void chooseGrabTarget(const sbot_msg::Position2D::ConstPtr& loc)
	{
		double offsetx, offsety;
		//Add offsets to position
		double x = double(loc->x);
		double y = double(loc->y);

		//calculate using relative position
		offsetx = 0;
		offsety = 0;

		grabposition.x = x + offsetx;
		grabposition.y = y + offsety;

		sbot_msg::Position2D posmsg;
		posmsg.x = grabposition.x;
		posmsg.y = grabposition.y;

		PositionPub.publish(posmsg);
	}

	void chooseDropTarget(const sbot_msg::TargetColor::ConstPtr& tcolor)
	{

	}

	void monitorEFState(const sbot_msg::EFStatus::ConstPtr& efstat)
	{}

public:
	SorterBotBBBCore()
	{
		SBState = READY;
		//advertise topics here
		PositionPub = n.advertise<sbot_msg::Position2D>("targetposition",1000);
		EFCommandPub = n.advertise<sbot_msg::EFCommand>("ef_command",1000);
		//subscribe topics here
		IPSub = n.subscribe("relativeposition", 1000, &SorterBotBBBCore::chooseGrabTarget,this);
		ColorSub = n.subscribe("targetcolor", 1000, &SorterBotBBBCore::chooseDropTarget,this);
		EFStatusSub = n.subscribe("ef_status", 1000, &SorterBotBBBCore::monitorEFState,this);
	}
};

int main(int argc, char **argv)
{
	ros::init(argc,argv,"bbb_core");

	SorterBotBBBCore BBBC;

	ros::spin();

	return 0;
}