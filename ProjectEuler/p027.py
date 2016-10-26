from u import is_prime as p

ma,mb,m=0,0,0
for a in xrange(-1000, 1001):
    for b in xrange(-1000, 1001):
        n = 0
        while True:
            if p(n*n + a*n + b):
                n+=1
            else:
                break
        if n > m:
            ma,mb,m=a,b,n
print ma*mb