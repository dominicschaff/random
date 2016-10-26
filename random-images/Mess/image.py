from PIL import Image, ImageDraw
from math import cos,sin,radians
import constants as c

spacing = 50
angle = radians(0)

def rotate(x,y, angle, offset=[0,0]):
    return [x * cos(angle) - y * sin(angle) + offset[0],x*sin(angle) + y*cos(angle) + offset[1]]

im = Image.new("RGB", (c.width, c.height), (0,0,0))

d = ImageDraw.Draw(im)

for i in xrange(spacing+1):
    xline = c.width - i*(c.width/spacing)
    yline = i*(c.height/spacing)
    d.line((xline,   0)        + (0,       yline), fill=(255,255,255), width=2)
    d.line((xline,   c.height) + (c.width, yline), fill=(255,255,255), width=2)

    d.line((xline,   0)        + (c.width,       c.height - yline), fill=(255,255,255), width=2)
    d.line((xline,   c.height) + (0, c.height - yline), fill=(255,255,255), width=2)

w = 255.0/c.width
h = 255.0/c.height
pixels = im.load()
for x in xrange(c.width):
    for y in xrange(c.height):
        i = x
        j = y
        if j > c.height/2:
            j = c.height - j
        if i > c.width/2:
            i = c.width - i
        if pixels[x,y] == (255,255,255):
            pixels[x,y] = ((int)(i*w),(int)(j*h),100)
        else:
            pass
            # pixels[x,y] = ((int)(255-i*w)/10,10,(int)(255-j*h)/10)
im.save('image1.png')
# im.show()