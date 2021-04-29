# -*- coding: utf-8 -*-
"""
Created: Apr 18 2021

@author: Ryan Clement

Day #3: Leap Year.
"""

print("Welcome to the Leap Year checker!")
year = int(input("Please enter a year: "))
n = "\n"
if year%4 == 0:
    if year%100 == 0:
        if year%400 == 0:
            print(n,year,"is a leap year.")
        else:
            print(n,year, "is not a leap year.")
    else:
        print(n,year,"is a leap year.")
else:
    print(n,year, "is not a leap year.")