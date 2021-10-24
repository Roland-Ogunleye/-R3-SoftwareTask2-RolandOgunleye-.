#!/usr/bin/env python3
from os import sep
import socket

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((socket.gethostname(), 5556))

while 1:
    data = s.recv(1024)  
    print(data.decode("utf-8"))
    if not data: break
    
     
        
