#!/usr/bin/python
import socket

host_name = socket.gethostname()

host_ip = socket.gethostbyname(host_name)

print host_ip
print host_name
