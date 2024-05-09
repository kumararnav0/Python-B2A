def square():
    a=int(input("Enter any integer"))
    print(f"The square of the number is {a*a} ")
def add() :
    a=int(input("Enter any integer"))
    b=int(input("Enter any number"))
    print(f"The sum of the numbers is {a+b} ")
def sub():
    a=int(input("Enter large integer")) 
    b=int(input("Enter small number"))
    print(f"The sutraction of the numbers is {a-b} ")
def product():
    a=int(input("Enter first number")) ,
    b=int(input("Enter second number"))
    print(f"The product of the numbers is {a*b} ")
def division():
    a=int(input("Enter first number")) 
    b=int(input("Enter second number"))
    print(f"The product of the numbers is {a/b} ")
def remainder():
    a=int(input("Enter the dividend")) 
    b=int(input("Enter the diviser "))
    print(f"The remainder of the division is {a%b} ")


m=input("What operation would you like to perform \n Addition(A),Subtraction(S1),Multiplication(M),Division(D),Square(S2),Remainder(R) \n Use code given in brackets as an input \n")
if(m=="A"):
    add()
if(m=="S1"):
    sub()
if(m=="M"):
    product()
if(m=="D"):
    division()
if(m=="S2"):  
    square() 
if(m=="R"):
    remainder()
else:
    print("Invalid input")    
