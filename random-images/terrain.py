from random import random
import sys
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

if len(sys.argv) == 3:
    SIZE = (int)(sys.argv[1])
    FILE_PREPEND = sys.argv[2]
else:
    print "usage: python <script_name>.py SIZE FILE_PREPEND"
    exit(1)

print "STARTING",FILE_PREPEND
WIDTH=2**SIZE+1

queue = []
block = np.zeros((WIDTH, WIDTH))
block[0, 0] = random()
block[0, WIDTH - 1] = random()
block[WIDTH - 1, 0] = random()
block[WIDTH - 1, WIDTH - 1] = random()

def f(a,b,c,d,l):
    added = False

    ab = (((b[0] - a[0])>>1) + a[0], a[1])
    ac = (a[0], ((c[1] - a[1])>>1) + a[1])
    bd = (b[0], ((d[1] - b[1])>>1) + b[1])
    cd = (((d[0] - c[0])>>1) + c[0], c[1])
    m = (ab[0], ac[1])
    if block[m] == 0:
        added = True
        block[m] = (block[a] + block[b] + block[c] + block[d])/4.0 + (random()*2.0-0.5)*2**(-l)

    if block[ab] == 0:
        added = True
        block[ab] = (block[a] + block[b])/2.0 + (random()*2.0-0.5)*2**(-l)

    if block[ac] == 0:
        added = True
        block[ac] = (block[a] + block[c])/2.0 + (random()*2.0-0.5)*2**(-l)

    if block[bd] == 0:
        added = True
        block[bd] = (block[b] + block[d])/2.0 + (random()*2.0-0.5)*2**(-l)

    if block[cd] == 0:
        added = True
        block[cd] = (block[c] + block[d])/2.0 + (random()*2.0-0.5)*2**(-l)

    if added:
        f(a, ab, ac, m,l+1)
        f(ab, b, m, bd,l+1)
        f(ac, m, c, cd,l+1)
        f(m, bd, cd, d,l+1)

f((0, 0), (WIDTH - 1, 0), (0, WIDTH - 1), (WIDTH - 1, WIDTH - 1), 0)

mpl.rcParams['toolbar'] = 'None'
fig = plt.figure(frameon=False, figsize=(50, 50))
ax = fig.gca(projection='3d')
surf = ax.plot_surface(np.arange(0, WIDTH, 1), np.arange(0, WIDTH, 1), block, cmap=mpl.cm.coolwarm,
        linewidth=0, antialiased=True)

fig.patch.set_visible(False)
ax.patch.set_visible(False)
ax.axis('off')
# plt.show()
plt.subplots_adjust(left=0.001, right=0.999, top=0.999, bottom=0.001)
print "SAVING...",FILE_PREPEND
for ii in xrange(0,360, 45):
    # print "Saving %03d/360"%(ii+1)
    ax.view_init(elev=45., azim=ii)
    with open('%s-%03d.png'%(FILE_PREPEND, ii), 'w') as outfile:
        fig.canvas.print_png(outfile, bbox_inches='tight')
ax.view_init(elev=90., azim=0)
with open('%s-top.png'%(FILE_PREPEND), 'w') as outfile:
    fig.canvas.print_png(outfile, bbox_inches='tight')
print "COMPLETE",FILE_PREPEND