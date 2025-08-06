#!/usr/bin/env pyhton3

import socket

server = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 8080

server.bind ((host, port))
server.listen (2)
print ("server is listening for incoming connections")

try:
    while True:
        conn,address = server.accept()
        print (f"connection received from {str(address)}")
        msg = "Connection established\r\n"
        conn.send(msg.encode('ascii'))
        conn.close()
except KeyboardInterrupt:
    print ("\nGoodbye my dear!")