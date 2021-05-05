"""
Created: May 4, 2021
@author: Ryan Clement
Day #10: Project: Calculator.
"""

from calculator_art import logo

print(logo)

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    '+':add,
    '-':subtract,
    '*':multiply,
    '/':divide
}

calc = True
new_calc = True
res = 0
while calc:
    if new_calc:
        num1 = float(input("What's the first number?: "))
    else:
        num1 = res
    for sym in operations:
        print(sym)
    op = input("Pick an operation from the line above: ")
    num2 = float(input("What's the second number?: "))
    res = operations[op](num1, num2)
    print(f"\n{num1} {op} {num2} = {res}\n")
    print(f"Type 'y' to continue calculating with {res},")
    print("or type 'n' to start a new calculation")
    print("or type 'q' to quit.")
    choice = input("Please enter your choice: ")
    if choice == 'q':
        calc = False
    elif choice == 'y':
        new_calc = False
    else:
        new_calc = True