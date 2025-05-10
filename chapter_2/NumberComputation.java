print('Number Computational')

FirstNumber = int(input('Enter a number: '))
SecondNumber = int(input('Enter a number: '))
ThirdNumber = int(input('Enter a number: '))


largest = FirstNumber
lowest = FirstNumber


if SecondNumber > largest:
    largest = SecondNumber
if ThirdNumber > largest:
    largest = ThirdNumber


if SecondNumber < lowest:
    lowest = SecondNumber
if ThirdNumber < lowest:
    lowest = ThirdNumber


total = FirstNumber + SecondNumber + ThirdNumber
product = FirstNumber * SecondNumber * ThirdNumber
average = total // 3  # Integer division


print("Sum:", total)
print("Product:", product)
print("Largest:", largest)
print("Lowest:", lowest)
print("Average:", average)
