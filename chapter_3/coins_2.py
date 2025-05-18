purchase_price = float(input("Enter the purchase price (less than or equal to $1.00): "))

if purchase_price < 0 or purchase_price > 1:
    print("Sorry, please enter a purchase price of $1.00 or below.")
elif purchase_price == 1.00:
    print("Your change is: 0 cents")
else:
    change = round(100 - (purchase_price * 100))

    quarters = change // 25
    change %= 25

    dimes = change // 10
    change %= 10

    pennies = change

    print("Your change is:")
    print(f"{quarters} quarter(s)")
    print(f"{dimes} dime(s)")
    print(f"{pennies} penn(y/ies)")
 