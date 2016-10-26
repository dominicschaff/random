#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define AMOUNT 250
#define WIDTH 480
#define HEIGHT 800
#define CHANCE 3
#define FRAMES 2

typedef struct {
	int x;
	int y;
	int rad;
	int dist;
	int colr;
	int colg;
	int colb;
	int p;
	int c;
	int t;

} point;

int main(int argc, char ** argv)
{
	point points[AMOUNT];

	int i =0;
	int j = 0;
	char filename[50];

	FILE *file;

	srand(time(NULL));
	int r = rand();
	double rm = WIDTH;
	if (HEIGHT < rm) {
		rm = HEIGHT;
	}
	rm /= 40.0;

	for (i = 0; i < AMOUNT; ++i)
	{
		points[i].x = rand()%WIDTH;
		points[i].y = rand()%HEIGHT;
		points[i].rad = rand()%((int)(rm*3)) + rm;
		points[i].dist = rand()%((int)(points[i].rad/2.0)) + points[i].rad/2.0;
		points[i].colr = rand()%250;
		points[i].colg = rand()%250;
		points[i].colb = rand()%250;
		points[i].p = 0;
		points[i].c = 1;
		points[i].t = rand()%10;
		if (points[i].t < CHANCE) {
			points[i].t = 0;
		} else {
			points[i].t = 1;
			points[i].dist/=10.0;
		}
	}


	//make all the frames
	for (j = 0; j < FRAMES; ++j)
	{
		for (i = 0; i < AMOUNT; ++i)
		{
			points[i].p += points[i].c;
			if (points[i].p >= points[i].rad) {
				points[i].c = -1;
			}
			if (points[i].p <=0) {
				points[i].c = 1;
			}
		}
		if (j < 10)
		{
			sprintf(filename,"movie-000%d.pos",j);
		} else if (j < 100) {
			sprintf(filename,"movie-00%d.pos",j);
		} else if (j < 1000) {
			sprintf(filename,"movie-0%d.pos",j);
		} else if (j < 10000) {
			sprintf(filename,"movie-%d.pos",j);
		}


		file = fopen(filename, "w");
		fprintf(file, "%d,%d\n", WIDTH,HEIGHT);
		for (i = 0; i < AMOUNT; ++i)
		{
			//t,x,y,r,d,r,g,b
			fprintf(file, "%d,%d,%d,%d,%d,%d,%d,%d\n", points[i].t, points[i].x, points[i].y, points[i].p, points[i].dist, points[i].colr, points[i].colg, points[i].colb);
		}
		fclose(file);
	}

}