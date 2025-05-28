import random

def generate_numbers(difficulty):
    if difficulty == 1:
        return random.randint(1, 9), random.randint(1, 9)
    else:
        return random.randint(10, 99), random.randint(10, 99)

def correct_response():
    responses = [
        "Very good!",
        "Nice work!",
        "Keep up the good work!"
    ]
    return random.choice(responses)

def incorrect_response():
    responses = [
        "No. Please try again.",
        "Wrong. Try once more.",
        "No. Keep trying."
    ]
    return random.choice(responses)

def generate_problem(difficulty, problem_type):
    x, y = generate_numbers(difficulty)

    if problem_type == 5: 
        problem_type = random.randint(1, 4)

    if problem_type == 1:
        question = f"How much is {x} plus {y}? "
        answer = x + y
    elif problem_type == 2:
        question = f"How much is {x} minus {y}? "
        answer = x - y
    elif problem_type == 3:
        question = f"How much is {x} times {y}? "
        answer = x * y
    elif problem_type == 4:
        x = x * y  
        question = f"How much is {x} divided by {y}? "
        answer = x // y
    else:
        question = "Invalid problem type."
        answer = None

    return question, answer

def call():
    try:
        difficulty = int(input("Enter difficulty level (1 = single-digit, 2 = two-digit): "))
        if difficulty not in [1, 2]:
            raise ValueError
    except ValueError:
        print("Invalid input. Defaulting to level 1.")
        difficulty = 1

    try:
        problem_type = int(input(
            "Select problem type:\n"
            "1 = Addition\n2 = Subtraction\n3 = Multiplication\n4 = Division\n5 = Random mix\n"
            "Your choice: "
        ))
        if problem_type not in [1, 2, 3, 4, 5]:
            raise ValueError
    except ValueError:
        print("Invalid input. Defaulting to random mix.")
        problem_type = 5

    while True:
        question, correct_answer = generate_problem(difficulty, problem_type)

        while True:
            try:
                user_input = int(input(question))
                if user_input == correct_answer:
                    print(correct_response())
                    break
                else:
                    print(incorrect_response())
            except ValueError:
                print("Please enter a valid integer.")

        again = input("Do you want to try another? yes/no: ").strip().lower()
        if again != "yes":
            print("Thanks for practicing!")
            break

call()
