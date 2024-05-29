print("The Love Calculator is calculating your score...")
name1 = input("Enter your name \n") # What is your name?
name2 = input("Enter your crush's name \n") # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
name=name1+name2
name=name.lower()

t=name.count('t')
r=name.count('r')
u=name.count('u')
e=name.count('e')
final1=t+r+u+e

l=name.count('l')
o=name.count('o')
v=name.count('v')
e=name.count('e')
final2=l+o+v+e

res=str(final1)+str(final2)
print(res)

res=int(res)
if(res<10 or res>90):
  print(f"Your score is {res}, you go together like coke and mentos.")
elif(40<res<50):
  print(f"Your score is {res}, you are alright together.")
else:
  print(f"Your score is {res}.")
  #this is how its done