# -*- coding: utf-8 -*-
"""
Created: Apr 15 2021

@author: Ryan Clement

Day #2: Project: Tip Calculator.
"""

print("Welcome to the tip calculator.")
totBill = float(input("What was the total bill? "))
tipPercent = int(input("What percentage tip would you like to give: 10, 12, or 15? "))
numPeople = int(input("How many people to split the bill? "))
totBill += totBill*tipPercent/100.0
print("\nEach person should pay: ${:.2f}".format(totBill/numPeople))