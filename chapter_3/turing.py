print("Welcome to the medical diagnosis system.")

input("What is your problem? ")

response = input("Have you had this problem before (yes or no)? ")

if response.lower() == "yes":
    print("Well, you have it again.")
elif response.lower() == "no":
    print("Well, you have it now.")
else:
    print("Sorry, I didn't understand your response.")
