#!/usr/bin/env pyhton3

import socket

server = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 8080

