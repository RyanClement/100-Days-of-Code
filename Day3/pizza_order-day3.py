# -*- coding: utf-8 -*-
"""
Created: Apr 18 2021

@author: Ryan Clement

Day #3: Pizza Order.
"""

bill = 0
print("Welcome to Python Pizza Deliveries!\n")
print("Available options and prices:")
print("Small Pizza: $15")
print("Medium Pizza: $20")
print("Large Pizza: $25")
print("Pepperoni for Small Pizza: +$2")
print("Pepperoni for Medium or Large Pizza: +$3")
print("Extra cheese for any size pizza: +$1")
size = input("What size pizza do you want? S, M, or L: ").upper()
add_pepperoni = input("Do you want pepperoni? (Y or N): ").upper()
extra_cheese = input("Do you want extra cheese? (Y or N): ").upper()
if size == "S":
    bill += 15
    if add_pepperoni == "Y":
        bill += 2
elif size == "M":
    bill += 20
    if add_pepperoni == "Y":
        bill += 3
else:
    bill += 25
    if add_pepperoni == "Y":
        bill += 3
if extra_cheese == "Y":
    bill += 1
print(f"\nYour final bill is: ${bill}")