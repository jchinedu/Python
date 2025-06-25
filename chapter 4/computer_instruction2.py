import random

def generate_question(difficulty):
    if difficulty == 1:
        return random.randint(1, 9), random.randint(1, 9)
    elif difficulty == 2:
        return random.randint(10, 99), random.randint(10, 99)
    else:
        print("Invalid difficulty level. Defaulting to level 1.")
        return random.randint(1, 9), random.randint(1, 9)

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

def cai_multiplication():
    try:
        difficulty = int(input("Enter difficulty level (1 = single-digit, 2 = two-digit): "))
    except ValueError:
        print("Invalid input. Defaulting to level 1.") 
        difficulty = 1

    while True:
        x, y = generate_question(difficulty)
        while True:
            try:
                answer = int(input(f"How much is {x} times {y}? "))
                if answer == x * y:
                    print(correct_response())
                    break
                else:
                    print(incorrect_response())
            except ValueError:
                print("Please enter a valid integer.")

        choice = input("Do you want to try another? yes/no: ").strip().lower()
        if choice != "yes":
            print("Thanks for practicing!")
            break

cai_multiplication()
