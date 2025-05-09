 largest = -999999999
second_largest = -999999999

for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest:
        second_largest = num

print("The largest number is:", largest)
print("The second largest number is:", second_largest)
