from math import *
from PIL import Image as I, ImageDraw as D
n=20
G=(1+5**.5)/2
w=int(G**(4*(n//4)))
i=I.new("RGB",(w,w),"white")
d=D.Draw(i)
k=pi/180
d.line([(G**(j/90)*cos(j*k)+w/2,G**(j/90)*sin(j*k)+w/2)for j in range(n*90)],fill=0)
i.save("s.png","PNG")