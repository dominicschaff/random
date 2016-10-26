import PIL.Image as Image
import PIL.ImageDraw as ImageDraw
from random import *
import sys
from math import cos, sin, pi, sqrt, tan

amount = 1
prepend = "wp-"
if len(sys.argv)>1:
    amount = int(sys.argv[1])
if len(sys.argv)>2:
    prepend = sys.argv[2]

#formulas:
def form_circle(x,y,i,d):
    return int(x + d*cos(i)),  int(y + d*sin(i))

def form_spiral(x, y, t, s):
    if t < 0: t=-t
    r = sqrt(t)
    if r == 0:
        r = 1.0
    else:
        r = 1.0/r
    return int(x+s*r*cos(t)), int(y+s*r*sin(t))

def form_loxodrome(x, y, t, s):
    c = tan (5*t)
    if c == 0: c = 1
    c = cos (1.0/c)
    x+=s*cos(t) * c
    y+=s*sin(t) * c
    return int(x), int(y)

#shapes:
def circle(id,c,r,f,col):
    for i in xrange(f):
        x0 = int(c[0] - r + i)
        x1 = int(c[0] + r - i)
        y0 = int(c[1] - r + i)
        y1 = int(c[1] + r - i)
        p = min((1.0, 1.0 * i / f + 0.3))
        n = (int(col[0] * p), int(col[1] * p), int(col[2] * p))
        id.ellipse((x0,y0,x1,y1),n)
    x0 = int(c[0] - r + f)
    x1 = int(c[0] + r - f)
    y0 = int(c[1] - r + f)
    y1 = int(c[1] + r - f)
    id.ellipse((x0,y0,x1,y1),col)

def arc(id, c, r, f, s, e, col):
    p=0.0
    for i in xrange(-f,f):
        x0 = int(c[0] - r + i)
        x1 = int(c[0] + r - i)
        y0 = int(c[1] - r + i)
        y1 = int(c[1] + r - i)
        if i < 0:
            p = 0.7 - 1.0 * i / f
        else:
            p = 0.7 - 1.0 * i / f
        p = min((1.0,p))
        n = (int(col[0] * p), int(col[1] * p), int(col[2] * p))
        id.pieslice((x0,y0,x1,y1), int(s + i), int(e - i), n)
        i += 1.0

def curve(pix, w, h, x0, y0, d, a, col):
    i = 0
    s = a*pi
    p=0.0
    while i < d:
        x,y = form_circle(x0,y0,i/s,d)
        #x,y = form_loxodrome(x0,y0,i/100.0, 100.0)
        for j in xrange(-d,+d):
            if j < 0:
                p = 0.7 + j / d
            else:
                p = 0.7 - j / d
            p = min((1.0,p))
            c2 = (int(col[0] * p), int(col[1] * p), int(col[2] * p))
            if x >= 0 and x < w and y+j >= 0 and y+j < h:
                pix[x,y+j] = c2
        i +=0.1




def makeImage(w,h,p,t):
    im = Image.new('RGB',(w,h),(0,0,0))
    pix = im.load()
    id = ImageDraw.Draw(im)
    rm = min(w,h)/50



    for i in xrange(p):
        x = randint(0,w)
        y = randint(0,h)
        r = randint(rm,rm*4)
        d = randint(r/4,r)
        c = (randint(35,255),randint(35,50),randint(35,255))
        if randint(0,10) <= t:
            circle(id, (x,y), r, d, c)
        else:
            curve(pix, w, h, x, y, r, d/10.0, c)
            #s = randint(0,180)
            #e = randint(s,180)
            #arc(id, (x,y), r, d, s, e, c)
    return im

#movie Functions
def makePoints(amount, width, height):
    return [[randint(0,10),randint(0,width-1), randint(0,height)] for i in xrange(amount)]

def applyTypeExtras(points, w, h, chance):
    rm = min(w,h)/40
    for i in xrange(len(points)):
        x = randint(0,w)
        y = randint(0,h)
        r = randint(rm,rm*4)
        d = randint(r/2,r)
        c = (randint(0,250),randint(0,250),randint(0,250))
        if points[i][0] <= chance:
            points[i][0] = 0
            points[i].append(r)
            points[i].append(d)
            points[i].append(c)
            points[i].append(0)
            points[i].append(1)
        else:
            points[i][0] = 1
            points[i].append(r)
            points[i].append(d/10.0)
            points[i].append(c)
            points[i].append(0)
            points[i].append(1)

def makeWallpapers(amount, prepend, width, height):
    for j in xrange(amount):
        makeImage(width,height,25, 10).save(prepend + str(j) + '.png')
        print "DONE:",j,'=(',(100.0*(j+1)/amount),'% complete)'

def makeMovie(amount, frames, prepend, width, height):
    points = makePoints(amount,width,height)
    applyTypeExtras(points, width, height, 100)
    for f in xrange(frames):
        im = Image.new('RGB',(width,height),(0,0,0))
        pix = im.load()
        id = ImageDraw.Draw(im)
        for i in xrange(amount):
            if points[i][0] == 0:
                points[i][6] += points[i][7]
                if points[i][6] > points[i][3]:
                    points[i][7] = -1
                if points[i][6] >= 0:
                    points[i][7] = 1
                circle(id, (points[i][1], points[i][2]), points[i][6], points[i][4], points[i][5])
            elif points[i][0] == 1:
                points[i][6] += points[i][7]
                if points[i][6] > points[i][3]:
                    points[i][7] = -1
                if points[i][6] >= 0:
                    points[i][7] = 1


                curve(pix, width, height, points[i][1], points[i][2], points[i][6], points[i][4], points[i][5])
        print "SAVING FRAME: %5d/%5d"%(f,frames)
        s = str(f)
        while len(s)<4:s="0"+s
        im.save(prepend+s+".png")


makeWallpapers(amount, prepend,2560,1600)