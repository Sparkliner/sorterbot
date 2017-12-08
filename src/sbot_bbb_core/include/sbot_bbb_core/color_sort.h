//This file contains the data required to sort all of the colors
//Edit the coordinates with the proper box for that color

#define SERVO_DELAY 5 //seconds
#define ORIGIN_X -30.0
#define ORIGIN_Y 60.0

struct BOX1{
	double x = -14;
	double y = 11;
};

struct BOX2{
	double x = -14;
	double y = -11;
};

struct NOBOX{
	double x = -14;
	double y = 20;
};

BOX1 BLACK;
BOX2 BLUE;
BOX1 RED;
BOX2 YELLOW;
BOX1 GREEN;
