# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 13:56:49 2021

@author: Marcin
"""

import socket

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

c = socket.socket()
c.connect(('localhost', 9999))

keyPair = RSA.generate(3072)

pubKey = keyPair.publickey()
print(f"Public key:  (n={hex(pubKey.n)}, e={hex(pubKey.e)})")
pubKeyPEM = pubKey.exportKey()
print(pubKeyPEM.decode('ascii'))

print(f"Private key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")
privKeyPEM = keyPair.exportKey()
print(privKeyPEM.decode('ascii'))

message = input("Enter your message: ")
encryptor = PKCS1_OAEP.new(pubKey)
encrypted = encryptor.encrypt(message)
print("Encrypted:", binascii.hexlify(encrypted))


c.send(bytes(encrypted, 'utf-8'))

print(c.recv(1024).decode())