import random

def guess_the_number():
    print("Guess my number between 1 and 1000 with the fewest guesses:")

    number_to_guess = random.randint(1, 1000)
    guess = None

    while guess != number_to_guess:
        try:
            guess = int(input("Your guess: "))
            if guess < number_to_guess:
                print("Too low. Try again.")
            elif guess > number_to_guess:
                print("Too high. Try again.")
            else:
                print("Congratulations. You guessed the number!")
        except ValueError:
            print("Please enter a valid integer.")

while True:
    guess_the_number()
    play_again = input("Would you like to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break
