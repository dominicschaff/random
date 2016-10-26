rt="""3
7 4
2 4 6
8 5 9 3"""
t=[[int(i) for i in s.split(" ")] for s in rt.split("\n")]

q=0
l=len(t)
for i in xrange(l):
    m = t[l-1][i]
    p=i
    for j in xrange(l-1, -1, -1):
        print j,p
        if p == 0:
            m+=t[j][p]
        elif p == len(t[j])-1:
            m+=t[j][p]
            p-=1
        else:
            if t[j][p] < t[j][p+1]:
                p+=1
            m+=t[j][p]
    if m>q:
        q=m
print q
