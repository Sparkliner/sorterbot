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
private:
	ros::NodeHandle n;

	ros::Publisher SBotStatusPub;
	ros::Publisher PositionPub;
	ros::Publisher EFCommandPub;

	ros::Subscriber ColorSub;
	ros::Subscriber EFStatusSub;
	ros::Subscriber IPSub;

	sbot_msg::SBotStatus sbstate;
	sbot_msg::Position2D grabposition;
	sbot_msg::Position2D dropposition;
	sbot_msg::EFCommand efcmd;

	void chooseGrabTarget(const sbot_msg::Position2D::ConstPtr& loc)
	{
		sbstate.status = sbot_msg::SBotStatus::SB_RETRIEVAL;

		double offsetx, offsety;
		//Add offsets to position
		double x = double(loc->x);
		double y = double(loc->y);

		//calculate using relative position
		offsetx = 0;
		offsety = 0;

		grabposition.x = x + offsetx;
		grabposition.y = y + offsety;

		//tell arm to move into position
		PositionPub.publish(grabposition);

		//notify end effector that it should get ready to grab
		efcmd.command = sbot_msg::EFCommand::CMD_GRAB;
		EFCommandPub.publish(efcmd);
	}

	void chooseDropTarget(const sbot_msg::TargetColor::ConstPtr& tcolor)
	{
		switch(tcolor->color) {
			case sbot_msg::TargetColor::BLACK:
				dropposition.x = BLACK.x;
				dropposition.y = BLACK.y;
				break;

			case sbot_msg::TargetColor::BLUE:
				dropposition.x = BLUE.x;
				dropposition.y = BLUE.y;
				break;

			case sbot_msg::TargetColor::RED:
				dropposition.x = RED.x;
				dropposition.y = RED.y;
				break;

			case sbot_msg::TargetColor::YELLOW:
				dropposition.x = YELLOW.x;
				dropposition.y = YELLOW.y;
				break;

			case sbot_msg::TargetColor::GREEN:
				dropposition.x = GREEN.x;
				dropposition.y = GREEN.y;
				break;
		}
	}

	void monitorEFState(const sbot_msg::EFStatus::ConstPtr& efstat)
	{
		if (efstat->status == sbot_msg::EFStatus::EF_READY)
		{
			//successfully picked up/dropped item
			if (sbstate.status == sbot_msg::SBotStatus::SB_RETRIEVAL)
			{
				//we got the item, let's deliver it now
				sbstate.status = sbot_msg::SBotStatus::SB_DELIVERY;
				//update target and signal arm to move
				PositionPub.publish(dropposition);
				//Notify end effector that it should get ready to drop
				efcmd.command = sbot_msg::EFCommand::CMD_DROP;
				EFCommandPub.publish(efcmd);
			}
			else if (sbstate.status == sbot_msg::SBotStatus::SB_DELIVERY)
			{
				//we've delivered the item, ready for the next one
				sbstate.status = sbot_msg::SBotStatus::SB_READY;

				//reset all our positions to avoid a mess
				grabposition.x = 0;
				grabposition.y = 0;

				dropposition.x = 0;
				dropposition.y = 0;

				//let home base know
				SBotStatusPub.publish(sbstate);
			}
		}
	}

public:
	SorterBotBBBCore()
	{
		sbstate.status = sbot_msg::SBotStatus::SB_READY;
		grabposition.x = 0;
		grabposition.y = 0;

		dropposition.x = 0;
		dropposition.y = 0;
		//advertise topics here
		PositionPub = n.advertise<sbot_msg::Position2D>("targetposition",1000);
		EFCommandPub = n.advertise<sbot_msg::EFCommand>("ef_command",1000);
		SBotStatusPub = n.advertise<sbot_msg::SBotStatus>("sbot_status",1000);
		//subscribe topics here
		IPSub = n.subscribe("relativeposition", 1000, &SorterBotBBBCore::chooseGrabTarget,this);
		ColorSub = n.subscribe("targetcolor", 1000, &SorterBotBBBCore::chooseDropTarget,this);
		EFStatusSub = n.subscribe("ef_status", 1000, &SorterBotBBBCore::monitorEFState,this);

		//publish that we're ready for our first item;
		SBotStatusPub.publish(sbstate);
	}
};

int main(int argc, char **argv)
{
	ros::init(argc,argv,"bbb_core");

	SorterBotBBBCore BBBC;

	ros::spin();

	return 0;
}