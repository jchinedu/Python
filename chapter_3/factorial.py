def factorial( n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n = int(input("Enter a nonnegative integer: "))

if n < 0:
    print("Please enter a nonnegative integer.")
else:
    fact = factorial(n)
    print(f"The factorial of {n} is {fact}")
