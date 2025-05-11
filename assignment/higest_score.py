num_students = int(input("Enter the number of students: "))

top_students = ""
highest_score = None

for i in range(num_students):
    name = input("Enter the student's name: ")
    score = float(input("Enter the student's score: "))

    if highest_score is None or score > highest_score:
        highest_score = score
        top_students = name
    elif score == highest_score:
        top_students = top_students + ", " + name

print("Student(s) with the highest score:")
print(top_students)
