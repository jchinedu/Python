def fahrenheit(celsius):
	return (9 / 5) * celsius + 32

print(f"{'Celsius':>10} {'Fahrenheit':>15  }")
print("-" * 26)

for c in range(0, 101):
    f = fahrenheit(c)
    print(f"{c:>10} {f:>15.1f}")
