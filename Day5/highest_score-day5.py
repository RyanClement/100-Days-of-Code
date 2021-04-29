# -*- coding: utf-8 -*-
"""
Created: Apr 25 2021

@author: Ryan Clement

Day #5: Highest Score.
"""

# Can't change block: start
student_scores = input("Input a list of student scores ").split()
for n in range(0,len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# Can't change block: stop
high_score = 0
for score in student_scores:
    if score > high_score:
        high_score = score
print("The highest score in the class is: {:d}".format(high_score))