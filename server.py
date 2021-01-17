# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 14:13:59 2021

@author: Marcin
"""

import socket


HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")
    
    msg = "Weclome to the server!"
    msg = f'{len(msg):<{HEADERSIZE}}' + msg
    
    clientsocket.send(bytes("Welcome to the server!", "utf-8"))
