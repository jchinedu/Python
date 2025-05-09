while True:
    n = int(input("Enter a positive integer: "))
    
    if n > 0:
        break
    else:
        print("Please enter a positive number.")

while n >= 1:
    print(n)
    n -= 1

print("Blast off!")
