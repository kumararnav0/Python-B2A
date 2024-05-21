#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
i=0
concat=''
for i in range(0,nr_letters):
    a=random.randint(0,len(letters)-1)
    
    # print(letters[a])
    concat=concat+str(letters[a])
print(concat)
concat1=''
for i in range(0,nr_numbers):
    a=random.randint(0,len(numbers)-1)
    
    # print(numbers[a])
    concat1=concat1+str(numbers[a])
print(concat1)
concat2=''
for i in range(0,nr_symbols)
    a=random.randint(0,len(symbols)-1)
    
    # print(symbols[a])
    concat2=concat2+str(symbols[a])
print(concat2)
    
# p=random.choices(letters[i])
# q=random.choices(numbers[i])
# r=random.choices(symbols[i])
# print(p+q+r)
password=concat+concat1+concat2
print(f"Your password is {password}")

#we can clearly see different level of indentation