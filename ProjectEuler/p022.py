f = open("p022_names.txt", "r")
n = []
for l in f:
    n += [i for i in l[1:-1].split("\",\"")]

a="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n.sort()

def v(f):
    t=0
    for i in f:
        t+= 1+a.index(i)
    return t
print sum([(1+i) * v(n[i]) for i in xrange(len(n))])
