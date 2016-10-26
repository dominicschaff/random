#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

#define WIDTH 2000
#define HEIGHT 2000
#define POINTS 100000
#define PI2 6.28318530718
#define PI 3.14159265359

int main(int argc, char const *argv[])
{
	int points,halfWidth,halfHeight,widthEnd,heightEnd,radius,x,y,r;
	double angle;
	FILE *f;
	srand(time(NULL));
	points = POINTS;
	halfWidth = WIDTH / 2;
	halfHeight = HEIGHT / 2;
	widthEnd = WIDTH - 1;
	heightEnd = HEIGHT - 1;
	radius = 0.99 * (halfWidth > halfHeight ? halfWidth : halfHeight);

	char pointMap[WIDTH][HEIGHT];

	//RESET:
	for (x = 0; x < WIDTH; ++x)
	{
		for (y = 0; y < HEIGHT; ++y)
		{
			pointMap[x][y] = 0;
		}
	}
	pointMap[halfWidth][halfHeight] = 1;

	while (points > 0) {
		printf("S\n");
		angle = ((rand() % 10000) / 10000.0) * PI2;
		x = (int)(cos(angle) * radius) + halfWidth;
		y = (int)(sin(angle) * radius) + halfHeight;
		while (1) {
			r = rand()%4;
			switch(r) {
				case 0:x++;break;
				case 1:x--;break;
				case 2:y++;break;
				case 3:y--;break;
			}
			if ((x <= 0) || (y <= 0) || (x >= widthEnd) || (y >= heightEnd))
				break;
			if (pointMap[x-1][y] || pointMap[x+1][y] || pointMap[x][y-1] || pointMap[x][y+1]) {
				pointMap[x][y] = 1;
				printf("E:%d\n", points);
				points--;
				break;
			}

		}
	}
	f = fopen(argv[1], "w");
	for (x = 0; x < WIDTH; ++x)
	{
		for (y = 0; y < HEIGHT; ++y)
		{
			if (pointMap[x][y])
				fprintf(f, "1");
			else
				fprintf(f, "0");
		}
		fprintf(f,"\n");
	}
	fclose(f);

	return 0;
}
