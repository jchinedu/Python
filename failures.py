passes = 0  
count = 0  

while count < 10:
    result = int(input('Enter result (1=pass, 2=fail): '))
    
    if result == 1:
        passes = passes + 1
        count = count + 1
    elif result == 2:
        count = count + 1
    else:
        print("Invalid input. Please enter 1 for pass or 2 for fail.")

failures = 10 - passes

print('Passed:', passes)
print('Failed:', failures)

if passes > 8:
    print('Bonus to instructor')
