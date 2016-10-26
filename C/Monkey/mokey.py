import random, string, time
import numpy as np
start = time.time()

letters = string.ascii_lowercase + ' '

script = open('Hamlet.txt','r') # opens the files
scriptRead = script.read()
script.close()
data = [letters.index(i) for i in scriptRead]

keyPresses = 0
monkeyTyped = ''
maxTyped = 0
totalKeyPresses = 0
print "Time Taken           | Max Characters | Total Key Presses"
while True:
    place = 0
    while np.random.randint(0,27) == data[place]:
        place=-~place
    keyPresses += place + 1
    if place > maxTyped:
        maxTyped = place
    if keyPresses > 1000000:
        totalKeyPresses += keyPresses
        keyPresses = 0
        d = time.time() - start
        print "%20.5f | %14d | %d | %f"%(d, maxTyped, totalKeyPresses, totalKeyPresses/d)