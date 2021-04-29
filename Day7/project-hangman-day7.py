# -*- coding: utf-8 -*-
"""
Created: Apr 26 2021

@author: Ryan Clement

Day #7: Project: Hangman.
"""
# Imports
import random
from hangman_art import stages as art
from hangman_art import logo
from hangman_words import word_list

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
    
# Begin Game
guesses = 0
max_guess = 6
guess_list = []
bad_guess = 0
print(logo)
word = random.choice(word_list)
print(art[-1])
state = make_state(word)
draw_state(state)
while bad_guess < max_guess:
    guess = input("Please guess a letter: ").lower()
    guess_list.append(guess)
    state, bad_guess = update_state(guess, bad_guess, state, word)
    print(art[-1-bad_guess])
    draw_state(state)
    if ''.join(''.join(state).split()) == word:
        win()
        break
    print_guess_list(guess_list)
    print(f'Number of incorrect guesses remaining: {max_guess-bad_guess}')
if bad_guess == max_guess:
    loose()
    print(f'Word: {word}')