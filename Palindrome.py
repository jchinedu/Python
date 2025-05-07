print('Palindrome checker')
number = int(input('enter a valid 5 digit number to check if it is palindrome or not: '))
if number < 10000 or number >99999:
    	print("invalid number, enter five digit")
else: 
	first_number = int(number // 10000)
	second_number = int(number // 1000) % 10
	fourth_number = int(number // 10) % 10
	fifth_number = int(number % 10)
if first_number == fourth_number & second_number == fifth_number:
        print("the number is palindrome")
else:
        print("the number is not a palindrome")

