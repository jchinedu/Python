principal = float(1000)
annual_rate = 0.07

for i in range(1, 31):
	print(f"{principal * ((1 + (annual_rate / 100)) **i):.2f}")