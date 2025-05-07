first_number = float(input("Enter first decimal: "))
second_number = float(input("Enter second decimal: "))
third_number = float(input("Enter third decimal: "))

if first_number <= second_number:
	if second_number <= third_number:
		print(f"""%.2f\n%.2f\n%.2f""" % (first_number, second_number, third_number))

if first_number <= third_number:
	if third_number <= second_number:
		print(f"""%.2f\n%.2f\n%.2f""" % (first_number, third_number, second_number))

if second_number <= first_number: 
	if first_number <= third_number:
		print(f"""%.2f\n%.2f\n%.2f""" % (second_number, first_number, third_number))

if second_number <= third_number:
	if third_number <= first_number:
		print(f"""%.2f\n%.2f\n%.2f""" % (second_number, third_number, first_number))

if third_number <= second_number:
	if second_number <= first_number:
		print(f"""%.2f\n%.2f\n%.2f""" % (third_number, second_number, first_number))

if third_number <= first_number:
	if first_number <= second_number:
		print(f"""%.2f\n%.2f\n%.2f""" % (third_number, first_number, second_number))



 