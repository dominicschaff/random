def divisors(n):
    return [i for i in xrange(n) if n%i == 0]
def count_divisors(n):
    z=0
    for i in xrange(1,n):
        if n%i==0:
            z+=1
    return z
def sum_divisors(n):
    z=0
    for i in xrange(1,n):
        if n%i==0:
            z+=i
    return z

def is_prime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True