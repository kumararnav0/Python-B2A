import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
a=input("Rock,Paper or Scissors?\n(R/P/S)\n")
print("Your move")
if(a=="R"):
    m=1
    print(rock)
elif(a=="P"):
    m=2
    print(paper)
elif(a=="S"):
    m=3
    print(scissors)
else:
         print("Invalid Input")
print("Opponent's move")
p=random.randint(1,3)
if (p==1):
    print(rock)
if(p==2):
    print(paper)
if(p==3):
    print(scissors)
else:
    ("Invalid issue")

if(a=="R" and p==1):
    print("It's a draw")
elif(a=="R" and p==2):
    print("You lose")  
elif(a=="R" and p==2):
    print("You won")    

elif(a=="P" and p==3):
    print("You lose")  
elif(a=="P" and p==1):
    print("You won")  
elif(a=="P" and p==2):
    print("It's a draw.")  

elif(a=="S" and p==1):
    print("You lose")  
elif(a=="S" and p==2):
    print("You won")  
elif(a=="S" and p==3):
    print("It's a draw.") 

