import socket
import sys
from random import randint
#/sbin/modprobe bic
#/sbin/modprobe highspeed
#/sbin/modprobe htcp
#/sbin/modprobe hybla
#/sbin/modprobe illinois
#/sbin/modprobe lp
#/sbin/modprobe probe
#/sbin/modprobe scalable
#/sbin/modprobe vegas
#/sbin/modprobe veno
#/sbin/modprobe westwood
#/sbin/modprobe yeah

if len(sys.argv) != 2:
    print "Correct usage: client.py <congestion type>"
    exit(0)

types = ['bic','highspeed','htcp','hybla','illinois','lp','probe','scalable','vegas','veno','westwood','yeah']

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.TCP_CONGESTION = 13
# sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_CONGESTION, types[int(sys.argv[1])])

server_address = ('h53.narga.sun.ac.za', 3005)
sock.connect(server_address)
data = ''
for i in xrange(1000):
    data += "%c"%chr(randint(42,112))

t = types[int(sys.argv[1])]
while len(t)<10:t = ' ' + t
try:
    sock.sendall(t)
    for x in xrange(2**5):
        sock.sendall(data)
finally:
    sock.shutdown(socket.SHUT_RDWR)
    sock.close()
