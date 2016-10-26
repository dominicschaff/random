from PIL import Image,ImageDraw
from random import randint
from sys import argv, exit
from math import pi

if len(argv) <= 1:
    print('We need a file')
    exit(1)

# setup some configs
ring_thickness, ring_spacing, colour_diff, quality, max_rings = 10, 5, pi, 10, 50

# some counters
ring, ring_size = 0, 0

# functions for readibility:
fix = lambda c: c if type(c) is int else ord(c)
fix_colour = lambda c: int(fix(c)*colour_diff%256)

# read in the file
text = ""
with open(argv[1], 'rb') as f:
    text = f.read()

l = len(text)

# the rings to draw, we start with one ring and nothing on it:
rings = [[(0,0,0,0)]]

# look at every fourth byte
for a in range(0, l, 4):
    # check if we can read forward by 3 bytes:
    if a + 3 < l:
        ring_size += fix(text[a])
        r = fix_colour(text[a+1])
        g = fix_colour(text[a+2])
        b = fix_colour(text[a+3])

        if ring_size > 360:
            rings[ring].append((360, r, g, b))
            ring_size -= 360
            ring+=1
            rings.append([(0,0,0,0)])
        rings[ring].append((ring_size, r, g, b))
    if ring > max_rings:
        break

# calculate some constants
amount_of_rings = len(rings)-1
size = (amount_of_rings + 1) * (ring_thickness + ring_spacing) * 2
half = size/2

# create image
image = Image.new("RGB", (size,size), (0,0,0))
draw = ImageDraw.Draw(image)

# draw the arcs
for ring, r in enumerate(rings[:-1]):
    b = (ring+1)*(ring_thickness + ring_spacing)
    s, e = half - b, half + b

    for arc in reversed(r):
        colour = (arc[1], arc[2], arc[3])
        for i in range(ring_thickness * quality):
            q = i/quality
            draw.arc((s + q,s + q, e - q, e - q), 0, arc[0], colour)
    print("Completed ring {} out of {}".format((ring+1), amount_of_rings))

# do the final output
if len(argv) > 2:
    image.save(argv[2], 'PNG')
else:
    for i, r in enumerate(rings[:-1]):
        print("Ring {}".format(i))
        for a in r:
            print("\t{}".format(a))
    image.show()