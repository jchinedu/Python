
pi = 0
sign = 1
i = 0
reached_3_14 = False
reached_3_141 = False
reached_3_1415 = False
reached_3_14159 = False
tolerance = 0.0001

print("Terms   Pi Approximation")

while True:
    pi = pi + sign * (4 / (2 * i + 1))
    print(i + 1, "     ", pi)

    # Check for each level of accuracy
    if not reached_3_14 and abs(pi - 3.14) < tolerance:
        print("Reached 3.14 at term:", i + 1)
        reached_3_14 = True

    if not reached_3_141 and abs(pi - 3.141) < tolerance:
        print("Reached 3.141 at term:", i + 1)
        reached_3_141 = True

    if not reached_3_1415 and abs(pi - 3.1415) < tolerance:
        print("Reached 3.1415 at term:", i + 1)
        reached_3_1415 = True

    if not reached_3_14159 and abs(pi - 3.14159) < tolerance:
        print("Reached 3.14159 at term:", i + 1)
        reached_3_14159 = True

    if reached_3_14 and reached_3_141 and reached_3_1415 and reached_3_14159:
        break

    sign = sign * -1
    i = i + 1
