print('Number Computational')

total = 0
product = 1

number = int(input('Enter number 1: '))
total = number
product = number
largest = number
lowest = number

for i in range(3):
    number = int(input(f'Enter number {i + 2}: '))
    total += number
    product *= number

    if number > largest:
        largest = number
    if number < lowest:
        lowest = number

average = total // 4

print("Sum:", total)
print("Product:", product)
print("Largest:", largest)
print("Lowest:", lowest)
print("Average:", average)
