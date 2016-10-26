from PIL import Image,ImageDraw,ImageFont
from random import randint
import sys

if len(sys.argv) < 2:
    print("You need at least 1 file as an argument")
    sys.exit(1)

files = sys.argv[1:]

# draw.textsize(14)
WIDTH,HEIGHT = 2000,2000
fullImage = Image.new("RGBA", (WIDTH,HEIGHT), (0,0,0,255))

pX,pY = 0,0 #-HEIGHT/10
i=1
onALine = 10
sX,sY = WIDTH/onALine,HEIGHT/(len(files)/(onALine))
for f in files:
    print("Busy With %s"%f)
    image = Image.new("RGBA", (WIDTH/2,HEIGHT), (0,0,0,0))
    draw = ImageDraw.Draw(image)
    draw.setfont(ImageFont.FreeTypeFont(file="UbuntuMono-R.ttf", size=20))
    fi = open(f, "r")
    c = (randint(100,200),randint(100,200),randint(100,200),200)
    y=15
    for line in fi:
        draw.text((20,y), line.strip(), fill=c)
        y+=15
    iT = image #image.rotate(randint(-15,15), resample=Image.BILINEAR, expand=True)
    fullImage.paste(iT, box=(pX,pY), mask=iT)
    if i >= onALine:
        i=1
        pX,pY = 0,pY+sY
    else:
        i+=1
        pX+=sX

fullImage.save("test.png")
