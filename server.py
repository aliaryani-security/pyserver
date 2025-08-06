#!/usr/bin/env pyhton3

import socket

server = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 8080

server.bind ((host, port))
server.listen (2)
print ("server is listening for incoming connections")