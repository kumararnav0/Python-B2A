import random
print('''Welcome to Number Guessing Game! \nI'm thinking of a number between 1 to 100 \nChoose a difficulty.Type 'easy' or 'hard': ''')
n=random.randint(1,100)
c=input("")
print(n)


if(c=="easy"):
    for i in range(1,11):
        m=int(input("Guess the number:\n"))
        if(m>n):
             print("Number too high\nGuess again:")
             print(f"You have {10-i} number of attempts remaining ") 
        elif(n>m):
             print("Number too low \nGuess again:")
             print(f"You have {10-i} number of attempts remaining ") 
        elif(m==n):
             print("You guessed the right number")    
             
             break
        else:
             print("Invalid input")
            
    i=i+1         
elif(c=="hard"):
    for i in range(1,6):
         m=int(input("Guess the number:\n"))
         if(m>n):
             print("Number too high\nGuess again:")
             print(f"You have {5-i} number of attempts remaining ") 
         elif(n>m):
             print("Number too low \nGuess again:")
             print(f"You have {5-i} number of attempts remaining ") 
         elif(m==n):
             print("You guessed the right number")  
             break
         else:
              print("Invalid input")
             
    i=i+1  
else:
    print("Invalid input")         
