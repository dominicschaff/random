from __future__ import division
from math import radians as rad, cos, sin
from PIL import Image, ImageDraw
from random import randint

width,height = 1280,1280

def randColour(s=0,e=255):
    return (randint(s,e),randint(s,e),randint(s,e))

def drange(start, stop, step):
    r = start
    while r < stop:
        yield r
        r += step

def convert(r,theta):
    return [r*cos(theta), r*sin(theta)]

def rotate(x,y, angle):
    return [x * cos(angle) - y * sin(angle),x*sin(angle) + y*cos(angle)]

class DrawImage(object):
    """docstring for DrawImage"""
    width = 1280
    height = 1280

    def __init__(self):
        self.size = (self.width, self.height)
        self.mid = (self.width/2, self.height/2)

    def create(self, size=(1280,1280), colour=(0,0,0)):
        self.image = Image.new("RGB", size, colour)
        self.pixels = self.image.load()
        self.size = size
        self.width = size[0]
        self.height = size[1]
        self.mid = (self.width/2, self.height/2)

    def open(self, name):
        self.image = Image.open(name)
        self.pixels = self.image.load()
        self.size = self.image.size
        self.width = self.size[0]
        self.height = self.size[1]
        self.mid = (self.width/2, self.height/2)

    def plot(self, spot, colour=(255,255,255)):
        x,y = spot[0], self.height - spot[1]
        if x >= self.width or y >= self.height:
            return
        if x<0 or y < 0:
            return
        self.pixels[x,y] = colour

    def plotRadians(self, function, start=0, end=100, offset=(0,0), steps=1.0, scale=1.0, colour=(255,255,255), rotation=0.0):
        for i in drange(start, end, steps):
            t = rad(i)
            r = function(t) * scale

            if type(r) is tuple:
                x,y = r
            else:
                x,y = convert(r,t)
            x,y = rotate(x,y,rad(rotation))
            self.plot((x+offset[0],y+offset[1]), colour)

    def addOver(self, image):
        for x in xrange(self.width):
            for y in xrange(self.height):
                if x < image.width and y < image.height and self.pixels[x,y] != (0,0,0):
                    image.plot((x,y), self.pixels[x,y])
        self.image = image.image
        self.pixels = image.pixels
        self.size = image.size
        self.width = image.width
        self.height = image.height

    def addUnder(self, image):
        w,h = image.size
        for x in xrange(image.width):
            for y in xrange(image.height):
                if x < w and y < h and image.pixels[x,y] != (0,0,0):
                    self.plot((x,y), image.pixels[x,y])

    def show(self):
        self.image.show()

    def save(self, name, imageType = None):
        if type is None:
            self.image.save(name)
        else:
            self.image.save(name, imageType)