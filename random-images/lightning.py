from random import randint
from PIL import Image,ImageDraw
import sys

PRE = "SHOW.png"
if len(sys.argv) == 2:
    PRE = sys.argv[1] + ".png"

WIDTH, HEIGHT = 1920,1080
COLOUR = (25,25,255)

image = Image.new("RGB", (WIDTH, HEIGHT), (0,0,0))
pixels = image.load()
pixels[randint(1,WIDTH-2),1] = COLOUR

def check(x,y):
    if x < 1 or y < 1 or x > WIDTH-2 or y > HEIGHT-2:
        return False
    if pixels[x-1,y] == COLOUR:
        return True
    if pixels[x+1,y] == COLOUR:
        return True
    if pixels[x,y-1] == COLOUR:
        return True
    if pixels[x,y+1] == COLOUR:
        return True
    return False

notComplete = True
while notComplete:
    x,y = randint(0,WIDTH-1),HEIGHT-1
    while not check(x,y):
        r = randint(0,2)
        if r == 0:
            x-=1
        elif r == 1:
            x+=1
        elif r == 2:
            y-=1
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            break
    if check(x,y):
        print "%s-> DOT: %d,%d"%(PRE,x,y)
        pixels[x,y] = COLOUR
    for i in xrange(WIDTH):
        if pixels[i,HEIGHT-2] == COLOUR:
            notComplete = False
            break


if len(sys.argv) == 2:
    image.save(sys.argv[1] + ".png")
else:
    image.show()