v = 20
while True:
    d = True
    for i in xrange(1, 21):
        if v%i!=0:
            d = False
            break
    if d:
        print v
        break
    if v%1000000==0:
        print 'done:',v
    v+=1
