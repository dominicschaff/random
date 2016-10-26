from random import random
from PIL import Image, ImageDraw

class Section(object):
    def __init__(self):
        self.level = 0
        self.left = 0
        self.right = 0
        self.heightLeft = 0
        self.heightRight = 0
    def __str__(self):
        return "(%f,%f) -> (%f,%f) [%d]"%(self.left, self.leftHeight, self.right, self.rightHeight, self.level)

DEPTH = 8
H = 0.7

queue = []
complete = []

s = Section()
s.left = 0
s.right = 1500
s.leftHeight = 0.0
s.rightHeight = 0.0

queue.append(s)

while len(queue) > 0:
    section = queue[0]
    queue = queue[1:]

    if section.level > DEPTH:
        complete.append(section)
        continue

    height = (section.leftHeight + section.rightHeight) / 2.0 + (random()*2.0*(2.0**(-H))**section.level - 0.5*(2.0**(-H))**section.level)

    s = Section()
    s.left = section.left
    s.right = (section.right - section.left)/2.0 + section.left
    s.level = section.level + 1
    s.leftHeight = section.leftHeight
    s.rightHeight = height
    queue.append(s)

    s = Section()
    s.right = section.right
    s.left = (section.right - section.left)/2.0 + section.left
    s.level = section.level + 1
    s.leftHeight = height
    s.rightHeight = section.rightHeight
    queue.append(s)

im = Image.new("RGB", (1500, 200), (0,0,0))
d = ImageDraw.Draw(im)
minHeight = min([min([s.leftHeight for s in complete]),min([s.rightHeight for s in complete])])
maxHeight = max([max([s.leftHeight for s in complete]),max([s.rightHeight for s in complete])])


for s in complete:
    lH = 150-(s.leftHeight*30)
    rH = 150-(s.rightHeight*30)
    d.line((s.left, lH) + (s.right, rH), fill=(255,255,255), width=1)

im.show()