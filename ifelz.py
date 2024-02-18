#if else statment examples
# if radius >= 0:
#  area = radius * radius * math.pi
#  print("The area for the circle of radius", radius, "is", area)
# else: 
#  print("Negative input")



#if else statement using random
#import random

# 1. Generate two random single-digit integers
# number1 = random.randint(0, 9) 
# number2 = random.randint(0, 9)

# 2. If number1 < number2, swap number1 with number2
# if number1 < number2: 
# number1, number2 = number2, number1 # Simultaneous assignment

# 3. Prompt the student to answer "What is number1 - number2?"
# answer = eval(input("What is "+ str(number1) + " - " + 
# str(number2) + "? "))

# 4. Check the answer and display the result
# if number1 - number2 == answer: 
#   print("You are correct!")
# else:
#   print("Your answer is wrong.\n", number1, '-',
# number2, "is", number1 - number2, '.')



# number = 30

# if number % 2 == 0: 
#  print(number, "is even.")
# else:
#  print(number, "is odd.")



#NESTED IF ELSE STATEMENT
# i = 8
# j = 9
# k = 5
# if i > k: 
#  if j > k: 
#   print("i and j are greater than k")
# else:
# print("i is less than or equal to k")



 #NESTED IF ELSE ELSE
# if score >= 90.0:
#    grade = 'A'
#     print(grade)
# else:
# if score >= 80.0:
#  grade = 'B'
#   print(grade)
# else:
#  if score >= 70.0:
#   grade = 'C'
#    print(grade)
#  else:
#   if score >= 60.0:
#    grade = 'D'
#      print(grade)
#   else:
#    grade = 'F'
#     print(grade)

#OR  IF ELIF ELSE can be used in place of if else else
#score = 90
#if score >= 90.0:
# grade = 'A'
# print(grade)
#elif score >= 80.0:
# grade = 'B'
# print(grade)
#elif score >= 70.0:
# grade = 'C'
# print(grade)
#elif score >= 60.0:
# grade = 'D'
# print(grade)
#else:
# grade = 'F'
# print(grade)

