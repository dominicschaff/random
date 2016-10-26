def c(s):
    c=1
    while s > 1:
        if s&1:
            s=3*s+1
        else:
            s=s>>1
        c+=1
    return c
m=0
n=1
for i in xrange(1000000):
    t=c(i)
    if t > m:
        m=t
        n=i
print n,m
