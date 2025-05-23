import random

def generate_question():
    return random.randint(1, 9), random.randint(1, 9)

def cai_multiplication():
    while True:
        x, y = generate_question()
        while True:
            try:
                answer = int(input(f"How much is {x} times {y}? "))
                if answer == x * y:
                    print("Very good!")
                    break
                else:
                    print("No. Please try again.")
            except ValueError:
                print("Please enter a valid integer.")

cai_multiplication()
