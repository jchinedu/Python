e_estimate = 1
factorial = 1
for i in range(1, 11):
    factorial *= i
    e_estimate += 1 / factorial
print("Estimated value of e after 10 terms:", e_estimate)
 