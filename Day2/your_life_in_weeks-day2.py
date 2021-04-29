# -*- coding: utf-8 -*-
"""
Created: Apr 15 2021

@author: Ryan Clement

Day #2: Your life in weeks.
"""

print('Welcome to Your Life In Weeks!')
years_old = int(input('Please enter your age in years: '))
years_left  = 90 - years_old
months_left = years_left*12
weeks_left  = years_left*52
days_left   = years_left*365
message = f'You have {days_left} days, {weeks_left} weeks and {months_left} months left.'
print('\nIf you live to 90 years...')
print(message)