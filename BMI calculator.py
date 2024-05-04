# Underweight: BMI less than 18.5
# Normal weight: BMI 18.5–24.9
# Overweight: BMI 25–29.9
# Obesity (Class I): BMI 30–34.9
# Obesity (Class II): BMI 35–39.9
# Obesity (Class III or severe obesity): BMI 40 or higher
weight=float(input("enter your weight in kilograms"))
height=float(input("enter your height in metres"))
bmi=round(weight/(height**2),2)
if(bmi<18.5):
  print(f"Your bmi is {bmi} and You're underweight.")

elif(18.5<=bmi<25):
  print(f"Your bmi is {bmi} and You have a normal weight.")

elif(25<=bmi<30):
  print(f"Your bmi is {bmi} and You're overweight.")

elif(30<=bmi<35):
  print(f"Your bmi is {bmi} and You have obesity(Class-I)")

elif(35<=bmi<40):
  print(f"Your bmi is {bmi} and You have obesity(Class-II)")

else:
   print(f"Your bmi is {bmi} and you have obesity (class III)")

