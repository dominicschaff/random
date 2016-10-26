t = 0
for a in xrange(0,201):
    for b in xrange(0,101):
        if a + b*2 <= 200:
            for c in xrange(0,41):
                if a + b*2 + c*5 <= 200:
                    for d in xrange(0,21):
                        if a + b*2 + c*5 + d*10 <= 200:
                            for e in xrange(0,11):
                                if a + b*2 + c*5 + d*10 + e*20 <= 200:
                                    for f in xrange(0,5):
                                        for g in xrange(0,3):
                                            for h in xrange(0,2):
                                                if a + b*2 + c*5 + d*10 + e*20 + f*50 + g*100 + h*200 == 200:
                                                    t+=1
print t
