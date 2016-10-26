def d(n):
    s=0
    for i in xrange(1,n):
        if n%i==0:
            s+=i
    return s
c=[]
z=0
f = [d(n) for n in xrange(10000)]
for i in xrange(10000):
    for j in xrange(10000):
        if i==j: continue
        if f[i] == j and f[j] == i:
            if (i,j) not in c and (j,i) not in c:
                print "ADDED: ", (i,j)
                c.append((i,j))
                z+=i+j
print z
