number = float(input("Enter a nonnegative integer: "))
if number < 1 or number > 10000:
    print("Please enter a number between 1 and 10000.")
else:
	total = 0
	while number > 0:
		total = total + (number % 10)
		number = number//10



print(f" the total of is {total}")