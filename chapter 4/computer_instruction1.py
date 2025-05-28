import random

def generate_question():
    return random.randint(1, 9), random.randint(1, 9)

def correct_response():
    responses = [
        "Very good!",
        "Nice work!",
        "Keep up the good work!"
    ]
    return responses[random.randint(0, 2)]

def incorrect_response():
    responses = [
        "No. Please try again.",
        "Wrong. Try once more.",
        "No. Keep trying."
    ]
    return responses[random.randint(0, 2)]

def cai_multiplication():
    while True:
        x, y = generate_question()
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
