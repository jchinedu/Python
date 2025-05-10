binary_input = int(input("Enter a binary number: "))
decimal_value = 0
position = 0
while binary_input > 0:
    digit = binary_input % 10
    if digit == 1:
        decimal_value += 2 ** position
    binary_input //= 10 
    position += 1 
print("The decimal equivalent is:", decimal_value)
