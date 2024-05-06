# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
  no_of_students=len(student_scores)

# Write your code below this row 👇
m=0
for i in range(0,no_of_students):
    if(m>student_scores[i]):
     # print(f"{m}>{student_scores[i]}")
      m=m
      
    elif(m<student_scores[i]):
     # print(f"{m}<{student_scores[i]}")
      m=student_scores[i]
    i=i+1    
   
print(f"The highest score in the class is: {m}")