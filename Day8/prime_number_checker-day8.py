# -*- coding: utf-8 -*-
"""
Created: Apr 28 2021

@author: Ryan Clement

Day #8: Prime Number Checker.
"""

def prime_checker(number):
    max = number//2 + 1
    for i in range(2,max):
        if number%i == 0:
            print(f"{number} is not a prime number.")
            return
    print(f"{number} is a prime number.")
    
print("Welcome to the prime number checker.")
n = int(input("Check this number: "))
prime_checker(n)