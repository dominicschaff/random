def is_prime(n):
    for i in xrange(2, n):
        if n%i == 0:
            return False
    return True

i = 1
p = 2
while i <= 10001:
    if is_prime(p):
        print "%5d > %d"%(i,p)
        i += 1
    p += 1
