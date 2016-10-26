def p(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

#def p(n):
#    if n==2:return True
#    if (n&1) == 0: return False
#    for i in xrange(3,n):
#        if n%i == 0:
#            return False
#    return True
t=0
for x in xrange(2, 2000000):
    if p(x):
        print x
        t+=x
print t
