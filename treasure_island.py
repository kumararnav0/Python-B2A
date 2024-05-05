line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("enter") # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
a=position
co_od1=a[0]
co_od2=a[1]
if(co_od1=="A"):
    co_od1=0
if(co_od1=="B"):
    co_od1=1
if(co_od1=="C"):
    co_od1=2
else:
    print("Invalid Input")
m=int(co_od1)  
n=int(co_od2)
n=n-1
map[m][n]="X"

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")