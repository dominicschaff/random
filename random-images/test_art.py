from random import random
from PIL import Image, ImageDraw
from math import sin, cos, radians

WIDTH, HEIGHT = 800, 800
COL = 79,195,247
POINTS = 50

im = Image.new("RGB", (WIDTH, HEIGHT), (0,0,0))
d = ImageDraw.Draw(im)


# points1 = [(i * WIDTH / (POINTS+1) + 10, 10) for i in xrange(POINTS)]
# points2 = [(10, i * HEIGHT / (POINTS+1) + 10) for i in xrange(POINTS)]

r = 200
circ = [(r*cos(radians(i)) + WIDTH/2, r*sin(radians(i)) + HEIGHT/2) for i in xrange(0, 360, 360/POINTS)]

l = len(circ)
for i in xrange(l*500):
    x = i%l
    y = (i + l/2 + 5)%l
    d.line(circ[x] + circ[y], fill=COL, width=1)
    d.line((WIDTH - circ[x][0], HEIGHT - circ[x][1]) + (WIDTH - circ[y][0], HEIGHT - circ[y][1]), fill=COL, width=1)

im.show()