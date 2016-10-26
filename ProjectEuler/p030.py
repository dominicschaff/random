from multiprocessing import Process, Queue

def work(s,e,q):
    q.put(sum([a for a,b in [(x,sum([int(i)**5 for i in str(x)])) for x in xrange(s,e)] if a==b]))

t = 10000000
q = Queue()

Process(target=work, args=(2,t/4,q)).start()
Process(target=work, args=(t/4,t/2,q)).start()
Process(target=work, args=(t/2,3*t/4,q)).start()
Process(target=work, args=(3*t/4,t,q)).start()
print sum([q.get(True) for i in xrange(4)])
