import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('0xc0de.co.za', 80))
mysock.send('GET http://0xc0de.co.za/index.html HTTP/1.0\n\n')
while True:
    data = mysock.recv(512)
    if(len(data)<1):
        break
    print data
mysock.close()
