t,i,m=0,1,0
while True:
    t+=i
    a=2+sum([1 for x in xrange(2,t) if t%x == 0])
    if a > m:
        m=a
        print i,t,m
    if a > 500:
        print t
        break
    i+=1
