from PIL import Image

im = Image.open("EncodedImage.bmp")

s = ''
zero = (80, 184, 72)
one = (87, 191, 79)
for y in range(73, 95):
    for x in range(453, 475):
        pix = im.getpixel((x,y))
        if pix == one:
            s+='1'
        elif pix == zero:
            s+='0'
        else:
            print(pix)

chunks = [s[i:i+8] for i in range(0, len(s), 8)]
for c in chunks:
    print(chr(int(c, 2)), end='')
print()
