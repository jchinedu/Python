def divisor(num, divisor)
number = int(input("How many numbers will you enter? "))
divisor = int(input("Enter the divisor: "))
result = []
for i in range(number):
    num = int(input("Enter number: "))
    if num % divisor == 0:
        result.append(num)
return print("Numbers divisible by", divisor, "are:", result)
