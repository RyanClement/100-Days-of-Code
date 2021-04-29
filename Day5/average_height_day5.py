# -*- coding: utf-8 -*-
"""
Created: Apr 25 2021

@author: Ryan Clement

Day #5: Average Height.
"""

# Can't change block: start
student_heights = input("Input a list of student heights ").split()
for n in range(0,len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)
# Can't change block: stop
average_height = 0
number_of_students = 0
for height in student_heights:
    average_height += height
    number_of_students += 1
average_height /= number_of_students
print("The average student height is {:.0f}cm.".format(average_height))