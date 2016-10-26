import PIL.Image as Image
import PIL.ImageDraw as ImageDraw
from random import *
import sys
from math import cos, sin, pi, sqrt, tan

w,h=1000,1000
im = Image.new('RGB',(w,h),(0,0,0))
pix = im.load()
id = ImageDraw.Draw(im)
mx,my=w/2,h/2


a,b=0,1
g=0
d=0
for i in xrange(15):
    a,b=b,a+b
    ax,ay=mx,my
    if d == 0:
        mx+=b
        my+=b
    elif d == 1:
        mx-=b
        my+=b
    elif d == 2:
        mx-=b
        my-=b
    elif d == 3:
        mx+=b
        my-=b
    d=(d+1)%4
    print (ax, ay, mx, my)
    id.arc((ax, ay, mx, my), g, g+90, (255,255,255)) #draw circle in black
    g+=90

im.show()