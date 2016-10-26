from PIL import ImageDraw, Image
from math import cos,sin,radians
from random import randint
import sys

a = "a0A1b2B3c4C5d6D7e8E9f!F,g.G/h?H<i>I:j;J'k\"K\\l|L/m M\nn\tN@o#O$p%P^q&Q*r(R)s_S-t+T=u{U}v[V]w W x X y Y z Z"
if len(a) > 128:
    print("TOO MANY CHARACTERS")
    sys.exit(1)

# for i in a:
#     print("%s -> %d %d %d %d %d %d %d "%(i,
#         1 if a.index(i) & 1 == 1 else 0,
#         1 if a.index(i) & 2 == 2 else 0,
#         1 if a.index(i) & 4 == 4 else 0,
#         1 if a.index(i) & 8 == 8 else 0,
#         1 if a.index(i) & 16 == 16 else 0,
#         1 if a.index(i) & 32 == 32 else 0,
#         1 if a.index(i) & 64 == 64 else 0,
#         ))

# sys.exit(0)
WHITE=(255,255,255)
PINK=(217,154,197)
BLUE=(103,170,249)
BLACK=(0,0,0)

img = Image.new('RGB', (2560,1600), BLACK)
id = ImageDraw.Draw(img)


def hex(offset, size):
    points = []
    x,y = offset
    for angle in range(0, 360, 60):
        x += cos(radians(angle)) * size
        y += sin(radians(angle)) * size
        points.append((x, y))
    return points

def drawHex(id, sx,sy,s,c):
    ox = sx - cos(radians(120)) * s
    oy = sy - sin(radians(120)) * s

    id.polygon(hex((ox-s,oy-s*2),s), fill=BLUE if c & 1 == 1 else PINK)
    id.polygon(hex((ox+s,oy-s*2),s), fill=BLUE if c & 2 == 2 else PINK)

    id.polygon(hex((ox-s*2,oy),s), fill=BLUE if c & 4 == 4 else PINK)
    id.polygon(hex((ox,oy),s), fill=BLUE if c & 8 == 8 else PINK)
    id.polygon(hex((ox+s*2,oy),s), fill=BLUE if c & 16 == 16 else PINK)

    id.polygon(hex((ox-s,oy+s*2),s), fill=BLUE if c & 32 == 32 else PINK)
    id.polygon(hex((ox+s,oy+s*2),s), fill=BLUE if c & 64 == 64 else PINK)

q = """This is a test
0123456789%"""
s = 10
cutOff = int(2560/(s*7))
print (cutOff)
x,y = 0,0
for c in q:
    drawHex(id, s*2 + x*s*7, s*3 + y*s*7, s, a.index(c))
    x+=1
    if x >= cutOff or c == "\n":
        x,y = 0,y+1
img.show()