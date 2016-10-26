b = 0
bx = 0
by = 0

for x in xrange(100, 1000):
    for y in xrange(100, 1000):
        a = x*y
        z = str(a)
        if z == z[::-1]:
            if a > b:
                b = a
                bx = x
                by = y

print b, bx, by