from random import randint, random
from PIL import Image,ImageDraw
from math import cos, sin, pi
import sys

PRE = "SHOW"
if len(sys.argv) == 2:
    PRE = sys.argv[1] + ".png"

WIDTH, HEIGHT = 1920,1080
COLOUR = (25,25,255)
RADIUS = 500
MID_X, MID_Y = WIDTH/2,HEIGHT/2

image = Image.new("RGB", (WIDTH, HEIGHT), (0,0,0))
pixels = image.load()
pixels[MID_X, MID_Y] = COLOUR

def checkBounds(x,y):
    if x < 0 or y < 0 or x > WIDTH-1 or y > HEIGHT-1:
        return True
    return False

def check(x,y):
    try:
        if pixels[x-1,y] == COLOUR:
            return True
        if pixels[x+1,y] == COLOUR:
            return True
        if pixels[x,y-1] == COLOUR:
            return True
        if pixels[x,y+1] == COLOUR:
            return True
    except Exception, e:
        pass
    return False

def move(x,y):
    r = randint(0,3)
    if r == 0:
        return x-1,y
    if r == 1:
        return x+1,y
    if r == 2:
        return x,y-1
    return x,y+1

def generate():
    r = random() * 2 * pi
    return int(MID_X + RADIUS * cos(r)), int(MID_Y + RADIUS * sin(r))

# PRETTY VERSION:
# x,y = generate()
# while True:
#     if checkBounds(x,y):
#         x,y = generate()
#         if check(x,y):
#             break
#         continue
#     if check(x,y):
#         print "DOT %d,%d"%(x,y)
#         pixels[x,y] = COLOUR
#         x,y = generate()
#         if check(x,y):
#             break
#         continue
#     x,y = move(x,y)

# FASTER VERSION
x,y = generate()
while True:
    if x < 0 or y < 0 or x > WIDTH-1 or y > HEIGHT-1:
        r = random() * 2 * pi
        x,y = int(MID_X + RADIUS * cos(r)), int(MID_Y + RADIUS * sin(r))
        if check(x,y):
            break
        continue
    if check(x,y):
        print "%s-> DOT: %d,%d"%(PRE,x,y)
        pixels[x,y] = COLOUR
        r = random() * 2 * pi
        x,y = int(MID_X + RADIUS * cos(r)), int(MID_Y + RADIUS * sin(r))
        if check(x,y):
            break
        continue
    r = randint(0,3)
    if r == 0:
        x-=1
    elif r == 1:
        x+=1
    elif r == 2:
        y-=1
    else:
        y+=1

if len(sys.argv) == 2:
    image.save(sys.argv[1] + ".png")
else:
    image.show()