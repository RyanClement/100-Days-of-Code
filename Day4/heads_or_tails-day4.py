# -*- coding: utf-8 -*-
"""
Created: Apr 18 2021

@author: Ryan Clement

Day #4: Heads or Tails.
"""

import random

print("Let's flip a virtual coin!")
rand_side = random.randint(0, 1)
if rand_side == 1:
    print("Heads")
else:
    print("Tails")
