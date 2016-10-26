import sys
def p(a,b,c):
    return (a*a + b*b) == (c*c)
def v(a,b,c):
    return (a+b+c) == 1000

for a in xrange(0,1000):
    print "a=",a
    for b in xrange(a+1,1000):
        for c in xrange(b+1,1000):
            if p(a,b,c) and v(a,b,c):
                print a,b,c,(a*b*c)
                sys.exit(0)
