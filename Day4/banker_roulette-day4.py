# -*- coding: utf-8 -*-
"""
Created: Apr 18 2021

@author: Ryan Clement

Day #4: Banker Roulette.
"""

import random

names = input("Give me everybody's names, seperated by a comma.\n").split(", ")
print(f"{names[random.randint(0, len(names)-1)]} is going to pay the bill today.")
