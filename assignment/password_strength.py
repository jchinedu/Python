password = input('enter a password: ')
length = len(password) 
if length < 8:
	print('the password is very weak')
else:
	if length == 8:
		print('the password is weak')
	if length >=8 and length <= 16:
		print('the password is Strong')
	if length > 16:
		print('the password is very strong')
  