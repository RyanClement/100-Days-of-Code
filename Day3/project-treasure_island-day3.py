# -*- coding: utf-8 -*-
"""
Created: Apr 18 2021

@author: Ryan Clement

Day #3: Project: Treasure Island.
"""

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island!")
print("Your mission is to find the treasure...\n")
print("""You're following your treasure map toward the big X along a trail in
a densly wooded forest and you've come to a bog that doesn't look safe
to cross. The trail goes left and right.""")
ans = input("Please choose left or right. L or R: ").upper()
if ans == 'R':
    print("""\nYou didn't notice the well concealed pit left by the local canibals.
You're dinner.
    *** Game Over! ***""")
else:
    print("""\nWalking around the bog you notice that it is just one end of a
lake. There is a boat dock ahead with a sign indicating rides to the other
side of the lake. However, you will have to wait for the boat to return.""")
    ans = input("Please choose swim or wait. S or W: ").upper()
    if ans == 'S':
        print("""\nAbout halfway across the lake you were attacked by a gang
of angry freshwater sharks armed with lazers. You're dinner.
    *** Game Over! ***""")
    else:
        print("""\nContinuing down the trail on the other side of the lake you
finally see your prize! The building marked on the map is now in your sight.
As you approach, you notice there are three doors. There is nothing on the map
about that... You know it is a test and you're just going to have to choose.
One door is red, one is blue, and the other is yellow.""")
        ans = input("Please choose the Red, Blue, or Yellow door. R, B, Y: ").upper()
        if ans == 'R' or ans == 'B':
            print("""\nNo one ever expects the zombie apocalypse. Zombies were
trapped behind that door. You're dinner.
    *** Game Over! ***""")
        else:
            print("\n$$$$$ You Win! $$$$$")