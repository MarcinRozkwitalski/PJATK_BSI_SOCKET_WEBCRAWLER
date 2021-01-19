# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 13:56:49 2021

@author: Marcin

Client side of project, it allows sending encrypted messages 
by Caesar Cipher Algorithm to server localhost on port 9999.
"""

import socket

alphabet = "abcdefghijklmnopqrstuvwxyz "
letter_to_index = dict(zip(alphabet, range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)), alphabet))

def encrypt(message, shift):
    cipher = ""
    # transverse the plain text
    for letter in message:
        # change letters to index by given shift
        number = (letter_to_index[letter] + shift) % len(letter_to_index)
        letter = index_to_letter[number]
        cipher += letter

    return cipher
        
def main():
    # do socket function on client (c)
    c = socket.socket()
    # connect to host named 'localhost' with port '9999'
    c.connect(('localhost', 9999))
    message = input("Enter message: ")
    encrypted_message = encrypt(message, 3)
    print("Encrypted message:",encrypted_message)
    # client sends message by utf-8 encoding
    c.send(bytes(encrypted_message, 'utf-8'))
    # print received message from server
    print(c.recv(1024).decode())

main()