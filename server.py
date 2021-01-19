# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 14:13:59 2021

@author: Marcin
"""

import socket


s = socket.socket()
print('Socket Created')

s.bind(('localhost', 9999))

s.listen(3)
print('waiting for connections')

while True:
    c, addr = s.accept()
    message = c.recv(1024).decode()
    print("Connected with ", addr, message)
    
    c.send(bytes('Server has successfully received your message','utf-8'))
    
    c.close()