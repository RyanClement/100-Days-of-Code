# -*- coding: utf-8 -*-
"""
Created: Apr 15 2021

@author: Ryan Clement

Day #2: BMI Calculator.
"""

print("Welcome to the Body Mass Index (BMI) Calculator.")
height = float(input("Enter your height in meters (m): "))
weight = float(input("Enter your weight in kilograms (kg): "))
print("\nBMI = ",int(weight/height**2))