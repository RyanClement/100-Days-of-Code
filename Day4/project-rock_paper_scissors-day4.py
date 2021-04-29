# -*- coding: utf-8 -*-
"""
Created: Apr 18 2021

@author: Ryan Clement

Day #4: Project: Rock-Paper-Scissors.
"""

import random

# Rules:
# Rock beats Scissors
# Scissors beats Paper
# Paper beats Rock

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

test = 0
rand_num = random.randint(0, 2) # Random Choice
print("Welcome to Rock, Paper, Scissors!\n")
req = "What do you choose? Type: 0 for Rock, 1 for Paper, or 2 for Scissors.\n"
user_num = int(input(req)) # User Choice    
if user_num == 0:
    user_choice = rock
    if rand_num == 0:
        rand_choice = rock
        res = "Draw."
    elif rand_num == 1:
        rand_choice = paper
        res = "You loose."
    else:
        rand_choice = scissors
        res = "You win."
elif user_num == 1:
    user_choice = paper
    if rand_num == 0:
        rand_choice = rock
        res = "You win."
    elif rand_num == 1:
        rand_choice = paper
        res = "Draw."
    else:
        rand_choice = scissors
        res = "You loose."
elif user_num == 2:
    user_choice = scissors
    if rand_num == 0:
        rand_choice = rock
        res = "You loose."
    elif rand_num == 1:
        rand_choice = paper
        res = "You win."
    else:
        rand_choice = scissors
        res = "Draw."
else:
    test = 1
if test:
    print("You chose an invalid number.")
else:
    print(f"You chose:\n{user_choice}")
    print(f"Computer chose:\n{rand_choice}\n")
    print(res)