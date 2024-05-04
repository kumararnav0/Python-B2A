print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
print("Game is solely based on your ability to make choices.")
a=input('Choose a Direction Left or Right(L/R) \n')
if(a=='R'):
    print("You fell into a hole. \n Your game is over")
elif(a=='L'):
    print("Congratulations you moved to next stage \n Choose whether to swim or wait.\n")
    b=input('S/W\n')
    if(b=='S'):
         print("You  were attacked by a trout \n Game Over")
    elif(b=="W"):
        print("Congratulation you moved to next stage ")
       
        c=input("Choose which colour door to walk into,Red(R)/Yellow(Y)/Blue(B)\n")
        if(c=="R"):
            print("You were burned by fire. \nGame Over")
        elif(c=="B"):
            print("You were eaten by beasts.\nGame Over")
        elif(c=="Y"):
             print('''Congratulations!!\nYou Won\n''')
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
        else:    
            print("Invalid Input\nGame Over")
    else:
         print("invalid input")   


else:
    print("invalid input")    