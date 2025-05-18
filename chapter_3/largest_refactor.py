first_num = int(input("enter a number: "))
largest = first_num
second_largest = -99999999999999999999999

for i in range(9):
    num = int(input(f"Enter number {i+2}: "))
    
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest:
        second_largest = num

print("The largest number is:", largest)
print("The second largest number is:", second_largest)
