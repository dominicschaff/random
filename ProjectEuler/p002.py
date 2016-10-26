ans = 0

a = 1
b = 2
while b < 4000000:
    if b & 1 == 0:
        ans += b
    a,b = b, a+b
print ans