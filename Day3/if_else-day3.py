# -*- coding: utf-8 -*-
"""
Created: Apr 18 2021

@author: Ryan Clement

Day #3: IF ELSE.
"""

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age in years? "))
    if age < 12:
        print("Child tickets are $5.")
        print("Pictures are an additional $3.")
        bill = 5
    elif age <= 18:
        print("Youth tickets are $7.")
        print("Pictures are an additional $3.")
        bill = 7
    elif age > 55 or age < 45:
        print("Adult tickets are $12.")
        print("Pictures are an additional $3.")
        bill = 12
    else:
        print("Mid-life crisis tickets are FREE!")
        print("Pictures are still an additional $3.")
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo.upper() == "Y":
        bill += 3
    print(f"Your final bill is ${bill}.")
else:
    print("Sorry, you have to grow taller before you can ride.")