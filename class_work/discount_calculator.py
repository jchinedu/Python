print('DISCOUNT CALCULATOR')
purchases = int(input('enter the amount of total purchase made, to calculate you discount: '))
if purchases < 1000:
	print("sorry insert an eligible purchase amount")
if purchases >= 1000 and purchases <= 10000:
	print("congratulations, you received 5% discount, here are your earning")
	discount = float(0.05 * purchases)
	print(f'the discount on your purchase is {discount:,.2f}$')
	new_purchase = int(purchases - discount)
	print(f'you new discounted purchase is {new_purchase:,.2f}$')

else:
	if purchases > 10000 and purchases <= 50000:
		print("congratulation, you received 10% discount, here are your earning")
		discount = float(0.1 * purchases)
		print(f'the discount on your purchase is {discount:,.2f}$')
		new_purchase = int(purchases - discount)
		print(f'you new discounted purchase is {new_purchase:,.2f}$')
	if purchases > 50000:
		print("congratulations, you received 20% discount, here are your earning")
		discount = float(0.1 * purchases)
		print(f"the discount on your purchase is {discount:,.2f}$")
		new_purchase = int(purchases - discount)
		print(f"you new discounted purchase is {new_purchase:,.2f}$")
