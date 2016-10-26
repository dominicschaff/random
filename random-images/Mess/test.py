from __future__ import division
from math import radians as rad, pi, e
from constants import *
import functions
import sys

dr = DrawImage()
dr.create()


dr.plotRadians(functions.butterfly,
    start    = 0,
    end      = 10000,
    offset   = (dr.width/2, dr.height/4),
    steps    = 0.1,
    scale    = 20,
    colour   = (18,182,252),
    rotation = 180)
print "Done: Butterfly"
dr.plotRadians(functions.butterfly,
    start    = 0,
    end      = 10000,
    offset   = (dr.width/2, dr.height/4*3),
    steps    = 0.1,
    scale    = 20,
    colour   = (18,182,252),
    rotation = 0)
print "Done: Butterfly"

dr.plotRadians(functions.butterfly,
    start    = 0,
    end      = 10000,
    offset   = (dr.width/4, dr.height/2),
    steps    = 0.1,
    scale    = 20,
    colour   = (18,182,252),
    rotation = 180)
print "Done: Butterfly"
dr.plotRadians(functions.butterfly,
    start    = 0,
    end      = 10000,
    offset   = (dr.width/4*3, dr.height/2),
    steps    = 0.1,
    scale    = 20,
    colour   = (18,182,252),
    rotation = 180)
print "Done: Butterfly"

for i in drange(50,70.5,0.5):
    dr.plotRadians(functions.leaf,
        start    = 0,
        end      = 10000,
        offset   = (dr.width/2, dr.height/2+25),
        steps    = 0.1,
        scale    = i,
        colour   = (252,18,252),
        rotation = 270)
    dr.plotRadians(functions.leaf,
        start    = 0,
        end      = 10000,
        offset   = (dr.width/2, dr.height/2+25),
        steps    = 0.1,
        scale    = i,
        colour   = (252,18,252),
        rotation = 90)
    print "Done: Leaf:", i

d2 = DrawImage()
d2.open('image1.png')
dr.addOver(d2)
dr.save('image3.png')