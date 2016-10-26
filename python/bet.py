from random import shuffle
BETS, PEOPLE = 100000, 100
HALF = PEOPLE/2 + 1
c = 0
boxes = range(PEOPLE)
for j in xrange(BETS):
    shuffle(boxes)
    sizes = []

    for i in xrange(PEOPLE):
        s = boxes[i]
        n = boxes[s]
        l = 1
        while n != i and n != s:
            l+=1
            n = boxes[n]
        if l not in sizes:
            sizes.append(l)
    if max(sizes) < HALF:
        c+=1
print 100.0 * c / BETS, "%"