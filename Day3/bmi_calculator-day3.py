# -*- coding: utf-8 -*-
"""
Created: Apr 18 2021

@author: Ryan Clement

Day #3: BMI Calculator (part 2).
"""

print("Welcome to the Body Mass Index (BMI) Calculator.")
height = float(input("Enter your height in meters (m): "))
weight = float(input("Enter your weight in kilograms (kg): "))
bmi = round(weight/height**2)
resp = "\nYour BMI is {:d}, You are {:s}"
if bmi < 18.5:
    print(resp.format(bmi,"underweight."))
elif bmi < 25:
    print(resp.format(bmi,"normalweight."))
elif bmi < 30:
    print(resp.format(bmi,"overweight."))
elif bmi < 35:
    print(resp.format(bmi,"obese."))
else:
    print(resp.format(bmi,"clinically obese."))