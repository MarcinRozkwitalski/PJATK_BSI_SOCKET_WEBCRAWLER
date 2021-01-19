# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 13:56:49 2021

@author: Marcin
"""

import socket

alphabet = "abcdefghijklmnopqrstuvwxyz "
letter_to_index = dict(zip(alphabet, range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)), alphabet))

def encrypt(message, shift=3):
    cipher = ""

    for letter in message:
        number = (letter_to_index[letter] + shift) % len(letter_to_index)
        letter = index_to_letter[number]
        cipher += letter

    return cipher
        
def main():
    c = socket.socket()
    c.connect(('localhost', 9999))
    message = input("Enter message: ")
    encrypted_message = encrypt(message, shift=3)
    print("Encrypted message:",encrypted_message)
    c.send(bytes(encrypted_message, 'utf-8'))
    print(c.recv(1024).decode())

main()