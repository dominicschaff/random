from u import sum_divisors as sd

z=0
ab=[i for i in xrange(1,28123/2 + 1) if sd(i) > i]
nums=[1 for i in xrange(28123+1)]
print sum(nums)
for a in ab:
    for b in ab:
        nums[a+b] = 0
print sum(nums)
for i in xrange(len(nums)):
    if nums[i]:
        z+=i
print z
