print('Number Spacing')

Number = int(input('Enter any five-digit number: '))

if Number < 10000 or Number > 99999:
    print("Invalid input. Please enter exactly a five-digit number.")
else:
    for i in range(5):
        digit = Number // (10**(4-i))
        Number = Number % (10**(4-i))
        print(f"{digit}", end="   ")
 