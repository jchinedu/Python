print("Multiplication table".center(40))
print("    ", end="")
for num in range(1, 10):
    print(f"{num:>4}", end="")
print()
print("    " + "-" * 36)

for row in range(1, 10):
    print(f"{row:>4}|", end="")
    for col in range(1, 10):
        print(f"{row * col:>4}", end="")
    print()
