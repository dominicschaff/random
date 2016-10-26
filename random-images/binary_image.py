import sys
from PIL import Image, ImageDraw
if len(sys.argv) < 2:
    print "Needs a filename"
    sys.exit(1)

filename = sys.argv[1]



f = open(filename, "rb")
f.seek(0, 2)
size = f.tell()
f.seek(0, 0)
#temp = [[ord(c) for c in i] for i in f]

dim = (int)((size/3)**0.5) + 1

print "Creating image %dx%d"%(dim,dim)
img = Image.new("RGB", (dim, dim), (0,0,0))

pix = img.load()
x,y = 0,0
while True:
    b = f.read(3)
    if b == None or len(b) == 0:
        break
    if len(b) < 3:
        continue
    pix[x,y] = (ord(b[0]), ord(b[1]), ord(b[2]))
    x+=1
    if x >= dim:
        print "Completed: %d/%d"%(y,dim)
        x,y = 0,y+1

#values = sum(temp, [])
#del temp
#print len(values)
f.close()
if len(sys.argv) == 3:
    img.save(sys.arv[2])
else:
    img.show()
