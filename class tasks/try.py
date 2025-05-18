number_1 = 5
number_2 = 0
quotient = 0

try:
	quotient = number_1 // number_2
except ZeroDivisionError as zde:
	print(zde)