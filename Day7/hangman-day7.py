# -*- coding: utf-8 -*-
"""
Created: Apr 26 2021

@author: Ryan Clement

Day #7: Project: Hangman.
"""

import random

# Functions
def make_state(word):
    state = []
    for ii in word:
        state.append('_ ')
    return state
    
def draw_state(state):
    print('\n',''.join(state))
    
def print_guess_list(guess_list):
    print(f"\nCurrent Guesses: {''.join(guess_list)}")

def update_state(guess,bad_guess,state,word):
    check = 1
    pos = 0
    for a in word:
        if a == guess:
            check = 0
            state[pos] = guess
        pos += 1
    if check:
        bad_guess += 1
    return state, bad_guess
        
def win():
    print('\nYou WIN!\n')
    
def loose():
    print("\nYou're HUNG!\n")

#Step 1 

word_list = ["aardvark", "baboon", "camel"]
guesses = 0

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
word = random.choice(word_list)
guess_list = []
bad_guess = 0
state = make_state(word)
draw_state(state)

while bad_guess < 5:
    #TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("Please guess a letter: ").lower()
    guess_list.append(guess)
    
    #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    state, bad_guess = update_state(guess, bad_guess, state, word)
    draw_state(state)
    if ''.join(''.join(state).split()) == word:
        win()
        break
    print_guess_list(guess_list)
    print(f'Number of incorrect guesses remaining: {5-bad_guess}')
if bad_guess == 5:
    loose()