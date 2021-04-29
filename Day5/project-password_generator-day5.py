# -*- coding: utf-8 -*-
"""
Created: Apr 25 2021

@author: Ryan Clement

Day #5: Project: Password Generator.
"""

#Password Generator Project
# Can't change code: start
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
# Can't change code: stop


easy_password = ''
hard_password = ''

# Method 1: Long
# rand_letters = ['']*nr_letters
# rand_numbers = ['']*nr_numbers
# rand_symbols = ['']*nr_symbols
# iLetNext = 0
# iNumNext = 0
# iSymNext = 0
# for iLet in range(nr_letters):
#     randN = random.randint(0, length_of_letters-1)
#     choice = letters[randN]
#     easy_password += choice
#     rand_letters[iLet] = choice
# for iSym in range(nr_symbols):
#     randN = random.randint(0, length_of_symbols-1)
#     choice = symbols[randN]
#     easy_password += choice
#     rand_symbols[iSym] = choice
# for iNum in range(nr_numbers):
#     randN = random.randint(0, length_of_numbers-1)
#     choice = numbers[randN]
#     easy_password += choice
#     rand_numbers[iNum] = choice
# for ii in range(password_length):
#     type = random.randint(1, 3)
#     if type == 1: #Letter
#         if iLetNext < nr_letters:
#             hard_password += rand_letters[iLetNext]
#             iLetNext += 1
#     elif type == 2: #Number
#         if iNumNext < nr_numbers:
#             hard_password += rand_numbers[iNumNext]
#             iNumNext += 1
#     elif type == 3: #Symbol
#         if iSymNext < nr_symbols:
#             hard_password += rand_symbols[iSymNext]
#             iSymNext += 1

# Method 2: Short
for iLet in range(nr_letters):
    easy_password += random.choice(letters)
for iSym in range(nr_symbols):
    easy_password += random.choice(symbols)
for iNum in range(nr_numbers):
    easy_password += random.choice(numbers)
for s in random.sample(easy_password, len(easy_password)):
    hard_password += s

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
print(f"Easy level password: {easy_password}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
print(f"Hard level password: {hard_password}")