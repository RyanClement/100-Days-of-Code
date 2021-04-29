# -*- coding: utf-8 -*-
"""
Created: Apr 28 2021

@author: Ryan Clement

Day #8: Paint Area Calculator.
"""
import math as m


# Calculates number of can of paint required to paint a wall of height (m)
# and width (m).
def paint_calc(height, width, cover):
    return m.ceil(height*width/cover)

print("Welcome to paint area calculator.")
print("Requested values are in meters.")
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5 # 1 can of paint covers "coverage" square meters of wall
num_cans = paint_calc(height=test_h, width=test_w, cover=coverage)
print(f"\n{num_cans} cans of paint are required.")