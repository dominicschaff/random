import itertools
p = itertools.permutations(range(10))
x = [i for i in p]
x.sort()
print ''.join(map(str, x[999999]))
