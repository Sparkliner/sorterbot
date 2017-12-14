//This file contains the data required to sort all of the colors
//Edit the coordinates with the proper box for that color

#define SERVO_DELAY 2 //seconds
#define ORIGIN_X -22.0
#define ORIGIN_Y 57.0

struct BOX1{
	double x = -35;
	double y = 30;
};

struct BOX2{
	double x = -35;
	double y = -15;
};

struct NOBOX{
	double x = 35;
	double y = 30;
};

NOBOX BLACK;
BOX2 BLUE;
NOBOX RED;
NOBOX YELLOW;
BOX1 GREEN;
