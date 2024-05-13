# Write your code below this line 👇
def prime_checker(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True



  



    
    
# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Enter the number")) # Check this number
if prime_checker(n):
  print("It's a prime number.")
else:
  print("It's not a prime number.")
