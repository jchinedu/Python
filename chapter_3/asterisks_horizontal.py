k = 10
for i in range(1, 11):	
	for star in range(i):
		print('*', end='')

	for space in range(i + k, 1, -1):
		print(' ', end='')
	
	for gap in range(3):
		print(' ', end='')
		
	for star in range(i + k, 1, -1):
		print('*', end='')

	for space in range(i):
		print(' ', end='')
		
	for gap in range(3):
		print(' ', end='')
	
	for space in range(i):
		print(' ', end='')

	for star in range(i + k, 1, -1):
		print('*', end='')
		
	for gap in range(3):
		print(' ', end='')
		
	for space in range(i + k, 1, -1):
		print(' ', end='')
	
	for space in range(i):
		print('*', end='')
	k -= 2
	print()

	 