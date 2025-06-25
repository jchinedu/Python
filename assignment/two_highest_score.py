num_students = int(input("Enter the number of students: "))

highest_score = None
second_highest_score = None
highest_students = ""
second_highest_students = ""

for i in range(num_students):
    name = input("Enter the student's name: ") 
    score = float(input("Enter the student's score: "))

    if highest_score is None or score > highest_score:
        second_highest_score = highest_score
        second_highest_students = highest_students

        highest_score = score
        highest_students = name
    elif score == highest_score:
        highest_students = highest_students + ", " + name
    elif second_highest_score is None or score > second_highest_score:
        second_highest_score = score
        second_highest_students = name
    elif score == second_highest_score:
        second_highest_students = second_highest_students + ", " + name

print("Student(s) with the highest score:")
print(highest_students)

print("Student(s) with the second highest score:")
print(second_highest_students)
