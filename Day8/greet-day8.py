# -*- coding: utf-8 -*-
"""
Created: Apr 28 2021

@author: Ryan Clement

Day #8: Greet.
"""

# Functions
def greet():
    print("Welcome to the greet function.")
    print("Hello...")
    print("I am a handy Python function!")
    
def greet_with_name(name):
    print(f"Hello {name}.")
    print(f"How do you do {name}?")
    
def greet_with(name, location):
    print(f"Hello {name}.")
    print(f"What is it like in {location}?")

# greet()    
# greet_with_name("Ryan")
greet_with("Ryan","Florida")

# Function call with keyword arguments
greet_with(location="Florida", name="Ryan")