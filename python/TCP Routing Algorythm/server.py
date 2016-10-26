import socket
import sys
from random import randint
import threading
import simple_plot as p

t1 = ''
t2 = ''
timingRun = threading.activeCount() + 1
piece = [0,0]
connected = 0
timeout = 0.1
dataSet = [[],[]]

def drawMe():
    global dataSet, timeout
    x1 = [x*timeout for x in xrange(len(dataSet[0]))]
    f = open((t1+','+t2+'.txt').replace(' ',''),'w')
    for t in xrange(len(dataSet[0])):
        s = str(x1[t]) + ' ' + str(dataSet[0][t]) + ' ' + str(dataSet[1][t]) + '\n'
        f.write(s)
    f.close()


class receiveThread (threading.Thread):
    def setThreadNum(self, s, connection):
        self.num = s
        self.connection = connection
    def run(self):
        global piece
        try:

            while True:
                data = self.connection.recv(1000)
                if len(data) == 0:break
                piece[self.num]+=1

        finally:
            self.connection.close()

#SETUP TIMER
def myTimer():
    global piece, timingRun, timeout
    p1, piece[0] = piece[0], 0
    p2, piece[1] = piece[1], 0

    p1 /= timeout
    p2 /= timeout
    p1 /= 1000.0
    p2 /= 1000.0
    dataSet[0].append(p1)
    dataSet[1].append(p2)
    if (timingRun  != threading.activeCount()) or (connected !=2):
        threading.Timer(timeout, myTimer).start()
    else:
        threading.Timer(0.5, drawMe).start()

threading.Timer(timeout, myTimer).start()
#END TIMER

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('h53.narga.sun.ac.za', 3005)
sock.bind(server_address)
sock.listen(2)
print 'Start First Engine'

connection1, client_address1 = sock.accept()
t1 = connection1.recv(10)
rt1 = receiveThread();
rt1.setThreadNum(0,connection1)
rt1.start()
connected+=1

print 'Start Second Engine'
connection2, client_address2 = sock.accept()
t2 = connection2.recv(10)
rt2 = receiveThread();
rt2.setThreadNum(1,connection2)
rt2.start()
connected+=1