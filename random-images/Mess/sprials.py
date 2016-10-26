from __future__ import division
from math import radians as rad, pi, e
from constants import *
import functions
import sys

dr = DrawImage()
dr.create((720,1280))

for theta in drange(0,1500, 30):
    r = functions.spiral(rad(theta))*6
    o = dr.mid
    d = convert(r,rad(theta))
    dr.plotRadians(functions.spiral,
        start    = 0,
        end      = 650,
        offset   = (o[0]+d[0], o[1]+d[1]),
        steps    = 0.1,
        scale    = r/100,
        colour   = randColour(100,200),
        rotation = theta-30)
    dr.plotRadians(functions.spiral,
        start    = 0,
        end      = 650,
        offset   = (o[0]+d[0], o[1]+d[1]),
        steps    = 0.1,
        scale    = r/100,
        colour   = randColour(100,200),
        rotation = theta-30+180)
    print 'Done: Sprirals: ',theta

for theta in drange(0,1500, 30):
    r = functions.spiral(rad(theta))*6
    o = dr.mid
    d = convert(r,rad(theta))
    d = rotate(d[0], d[1], rad(180))
    dr.plotRadians(functions.spiral,
        start    = 0,
        end      = 650,
        offset   = (o[0]+d[0], o[1]+d[1]),
        steps    = 0.1,
        scale    = r/100,
        colour   = randColour(100,200),
        rotation = theta-30)
    dr.plotRadians(functions.spiral,
        start    = 0,
        end      = 650,
        offset   = (o[0]+d[0], o[1]+d[1]),
        steps    = 0.1,
        scale    = r/100,
        colour   = randColour(100,200),
        rotation = theta-30+180)
    print 'Done: Sprirals: ',theta

# d2 = DrawImage()
# d2.open('image1.png')
# dr.addOver(d2)
# dr.save('image2.png', 'PNG')
dr.show()