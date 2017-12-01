#include "ros/ros.h"
#include "sbot_msg/Position2D.h"
#include "sbot_msg/EFCommand.h"
#include "sbot_msg/EFStatus.h"
#include "sbot_msg/TargetColor.h"
#include "sbot_msg/SBotStatus.h"
#include <string>

enum class SysState {
	READY, RETRIEVAL, DELIVERY
};

class SorterBotBBBCore()
{
public:
	SysState SBState;

	SorterBotBBBCore()
	{
		SBState = SysState::READY;
	}
}