a,b,c=0,1,1
for i in xrange(1,10000):
    if len(str(c)) >= 1000:
        print i
        break
    c=b+a
    a=b
    b=c
