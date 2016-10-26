val = 600851475143
b = 2
i = 2
v = []
while val > 1:
    while val % i == 0:
        val /= i
        v.append(i)
    if i > b:
        b = i
    i+=1
v = list(set(v))
print b
print v