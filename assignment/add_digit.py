def digit_add(number):
	if number < 1 and number > 10000:
		print('sorry, insert a valid number between 1 and 1000')

	total = 0
	while number > 0:
		total = total + (number % 10)
		number = number//10
	return total

number = float(input("Enter a nonnegative integer: "))
if number < 1 or number > 10000:
    print("Please enter a number between 1 and 10000.")
else:
    Addition = digit_add(number)
    print(f"The total of {number} is {Addition}")
