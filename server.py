# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 14:13:59 2021

@author: Marcin

Server side of project, it listens on port 9999.
It allows receiving encrypted messages by Caesar Cipher Algorithm.
"""

import socket

s = socket.socket()
print('Socket Created')
# create host named 'localhost' with port '9999'
s.bind(('localhost', 9999))
s.listen(3)
print('Waiting for connections...')

while True:
    c, addr = s.accept()
    # decoding received message from client
    message = c.recv(1024).decode()
    print("Connected with ", addr, message)
    # send to client 
    c.send(bytes('Server has successfully received your message','utf-8'))
    # close connection to client
    c.close()