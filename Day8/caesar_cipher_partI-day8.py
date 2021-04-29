# -*- coding: utf-8 -*-
"""
Created: Apr 28 2021

@author: Ryan Clement

Day #8: Caesar Cipher Part I.
"""
# DATA
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# FUNCTIONS
def encrypt(text, shift):
    cryp = ''
    for c in text:
        pos = alphabet.index(c) + shift
        if pos < 25:
            cryp += alphabet[pos]
        else:
            pos -= 26
            cryp += alphabet[pos]
    return cryp

def decrypt(text, shift):
    cryp = ''
    for c in text:
        pos = alphabet.index(c) - shift
        cryp += alphabet[pos]
    return cryp


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

if direction == "encode" or direction == "decode":
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == "encode":
        eText = encrypt(text, shift)
        print(f"\nEncrypted message: {eText}")
    elif direction == "decode":
        eText = decrypt(text, shift)
        print(f"\nDecrypted message: {eText}")
else:
    print(f"\nWhat is {direction}?")
