# -*- coding: utf-8 -*-
"""
Created: Apr 28 2021

@author: Ryan Clement

Day #8: Caesar Cipher Part II.
"""
# DATA
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# This is not what she wanted but it does work...
# FUNCTIONS
# def encrypt(text, shift):
#     cryp = ''
#     for c in text:
#         pos = alphabet.index(c) + shift
#         if pos < 25:
#             cryp += alphabet[pos]
#         else:
#             pos -= 26
#             cryp += alphabet[pos]
#     return cryp

# def decrypt(text, shift):
#     cryp = ''
#     for c in text:
#         pos = alphabet.index(c) - shift
#         cryp += alphabet[pos]
#     return cryp

# def ceasar(choice, text, shift):
#     fun = globals()['encrypt']
#     return fun(text, shift)

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
# eText = ceasar(direction, text, shift)
# print(f"\nResulting message: {eText}")

# What she wanted...
# FUNCTIONS
def ceasar(choice, text, shift):
    cryp = ""
    for c in text:
        pos = alphabet.index(c)
        if choice == "encode":
            pos += shift
            if pos < 25:
                cryp += alphabet[pos]
            else:
                pos -= 26
                cryp += alphabet[pos]
        elif choice == "decode":
            pos -= shift
            cryp += alphabet[pos]
    print(f"\n{choice}d message: {cryp}")

# MAIN
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
ceasar(direction, text, shift)