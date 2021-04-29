# -*- coding: utf-8 -*-
"""
Created: Apr 18 2021

@author: Ryan Clement

Day #4: Treasure Map.
"""

row1 = ['#','#','#']
row2 = ['#','#','#']
row3 = ['#','#','#']
map = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
# Note: ColumnRow
position = input("Where do you want to put the treasure? ")
col = int(position[0]) - 1
row = int(position[1]) - 1 
map[row][col] = 'X'
print(f"{map[0]}\n{map[1]}\n{map[2]}")