age = int(input("Enter your age: "))
maximum_heart_rate = 220 - age
first_range = maximum_heart_rate * 0.50
second_range = maximum_heart_rate * 0.85

print("""Your maximum heart rate is %d beats per minute
Your target heart rate is %.2f-%.2f%%""" % (maximum_heart_rate, first_range, second_range))