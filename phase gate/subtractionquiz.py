import random
print('welcome to the subtraction quiz game')
totalQuestions = 10
score = 0
count = 0
print("Subtraction Quiz: You have  ", totalQuestions , "  questions!");
for i in range (totalQuestions):
 num1 = random.randint(1, 50)
 num2 = random.randint(1, 50)
 if num2 > num1:
   num2 = num1
 correctAnswer = int(num1 - num2)
 print("Question  ", i , " : What is  " ,  num1  , " - " , num2 , "? ");
 userAnswer = int(input('enter the answer: '))
 if userAnswer == correctAnswer:
  print("Correct!");
  score = score + 1
 else:
  print("Incorrect.");
 if userAnswer != correctAnswer:
  print('you have one more chance')
  print("Question  ", i  ," : What is  ", num1,  "  -  " , num2,  "? ");
  userAnswer = int(input('enter the answer: '))
 

print("\nYour final score: ",  score , " out of " , totalQuestions);
 
