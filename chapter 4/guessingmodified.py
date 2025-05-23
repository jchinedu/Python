import random

def guess_the_number():
    print("Guess my number between 1 and 1000. You have 10 tries:")

    number_to_guess = random.randint(1, 1000)
    attempts = 0
    max_attempts = 10

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low. Try again.")
            elif guess > number_to_guess:
                print("Too high. Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempt(s).")
                if attempts <= 10:
                    print("Either you know the secret or you got lucky!")
                return
        except ValueError:
            print("Please enter a valid whole number.")
    
    print(f"\nYou've used all {max_attempts} attempts. The number was {number_to_guess}.")
    print("You should be able to do better!")

while True:
    guess_the_number()
    play_again = input("Would you like to play again? (yes/no): ").strip().lower()
    if play_again != 'yes':
        print("Thanks for playing!")
        break
