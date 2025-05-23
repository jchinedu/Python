def fahrenheit(celsius):
	return (9 / 5) * celsius + 32

print(f"{'Celsius':>15} {'Fahrenheit':>20}")
print("-" * 26)

for c in range(0, 101):
    f = fahrenheit(c)
    print(f"{c:>15} {f:>20.1f}")
