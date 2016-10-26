from __future__ import division
from math import radians as rad, pi, e
from constants import *
import functions
import sys

dr = DrawImage()
dr.create()

for theta in drange(0,360, 30):
    s = 1.0
    for r in drange(50, 300, 50):
        o = dr.mid
        d = convert(r,rad(theta))
        dr.plotRadians(functions.spiral,
            start    = 0,
            end      = 720,
            offset   = (o[0]+d[0], o[1]+d[1]),
            steps    = 0.01,
            scale    = s/4,
            colour   = (252,18,18),
            rotation = theta+90)
        dr.plotRadians(functions.spiral,
            start    = 0,
            end      = 720,
            offset   = (o[0]+d[0], o[1]+d[1]),
            steps    = 0.01,
            scale    = s/4,
            colour   = (252,18,18),
            rotation = theta+90+180)
        s+=1
    print 'Done: Sprirals: ',theta


dr.plotRadians(functions.butterfly,
    start    = 0,
    end      = 10000,
    offset   = (dr.width/2, dr.height/4),
    steps    = 0.1,
    scale    = 20,
    colour   = (18,182,252),
    rotation = 180)
print "Done: Butterfly"

for i in drange(10,15.5,0.5):
    dr.plotRadians(functions.leaf,
        start    = 0,
        end      = 10000,
        offset   = (dr.width/2, dr.height/2+25),
        steps    = 0.1,
        scale    = i,
        colour   = (252,18,252),
        rotation = 180)
    print "Done: Leaf:", i
d2 = DrawImage()
d2.open('image2.png')
dr.addOver(d2)
dr.save('image3.png', 'PNG')