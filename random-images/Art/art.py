import PIL.Image as Image
import PIL.ImageDraw as ImageDraw
from random import randint,random
from math import pi,cos,sin
import sys

if len(sys.argv) != 3:
	print 'You are an idiot'
	exit()
pointMap = []

f = open(sys.argv[1])

for line in f:
	pointMap.append([])
	for c in line:
		pointMap[-1].append(c == '1' and True or False)


image = Image.new('RGB', (len(pointMap),len(pointMap[0])), (0,0,0))
pix = image.load()
for x in xrange(len(pointMap)):
	for y in xrange(len(pointMap[x])):
		if pointMap[x][y]:
			pix[x,y] = (255,255,255)

image.save(sys.argv[2])