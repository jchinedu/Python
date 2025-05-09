print('RETURN ON INVESTMENT CALCULATOR')
investment_amount = float(input('enter the investment amount: '))
if investment_amount < 0 :
	print(' investment can not be less than zero, please input a valid investment amount')
number_of_years = int(input('enter the number of years: '))
interest_rate = float(input('enter the interest rate: ')) / 100
for i in range(0, number_of_years, 1):
	interest = (float(investment_amount * interest_rate))
	investment_amount = investment_amount + interest 
	print(f"the return of investment over the {i+1} year(s)  is ${investment_amount:,.2f}")
	
