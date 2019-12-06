#! /usr/bin/python3
import socket
def getOS():
   x = socket.gethostname()
   return x 
print(getOS())
