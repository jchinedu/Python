purchase_price = float(input("Enter the purchase price (less than or equal to $1.00): "))

if purchase_price < 0 or purchase_price > 1:
    print("Sorry, please enter a purchase price of $1.00 or below.")
elif purchase_price == 1.00:
    print("Your change is: 0 cents")
else:
    change = round(100 - (purchase_price * 100))

    quarters = change // 25
    change = change % 25

    dimes = change // 10
    change = change % 10

    nickels = change // 5
    change = change % 5

    pennies = change // 1

    print("Your change is:")
    if quarters > 0:
        print(f"{quarters} quarter{'s' if quarters > 1 else ''}")
    if dimes > 0:
        print(f"{dimes} dime{'s' if dimes > 1 else ''}")
    if nickels > 0: 
        print(f"{nickels} nickel{'s' if nickels > 1 else ''}")
    if pennies > 0:
        print(f"{pennies} penn{'ies' if pennies > 1 else 'y'}")
