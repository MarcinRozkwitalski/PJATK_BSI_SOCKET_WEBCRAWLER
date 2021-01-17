# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 13:56:49 2021

@author: Marcin
"""

import socket

c = socket.socket()

c.connect(('localhost', 9999))

message = input("Enter your message: ")
c.send(bytes(message, 'utf-8'))

print(c.recv(1024).decode())