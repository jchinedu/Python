def atm_system():
    transactions = []

    try:
        balance = float(input("Enter your starting account balance (₦): "))
        if balance < 100:
            print("You must start with at least ₦100.")
            return
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return

    while True:
        print("\n=== welcome to SEMICOLON ATM ===")
        print("1. Withdraw")
        print("2. View Transaction Log")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            try:
                amount = float(input("Enter withdrawal amount (₦): "))
            except ValueError:
                print("Invalid input. Enter a number.")
                continue

            if amount % 500 != 0:
                print("Withdrawal must be in multiples of ₦500 or ₦1000.")
                continue

            withdrawal_fee = 100
            total_deduction = amount + withdrawal_fee
            max_withdrawable = balance * 0.9

            if amount > max_withdrawable:
                print(f"You cannot withdraw more than 90% of your balance (₦{max_withdrawable:.2f}).")
            elif balance - total_deduction < 100:
                print("Insufficient balance. At least ₦100 must remain in the account after withdrawal.")
            else:
                balance -= total_deduction
                print(f"\n--- TRANSACTION SUCCESSFUL ---")
                print(f"Amount Withdrawn : ₦{amount:.2f}")
                print(f"Withdrawal Fee   : ₦{withdrawal_fee:.2f}")
                print(f"Remaining Balance: ₦{balance:.2f}")

                transactions.append({
                    "withdrawn": amount,
                    "fee": withdrawal_fee,
                    "balance": balance
                })

        elif choice == '2':
            print("\n=== TRANSACTION LOG ===")
            if not transactions:
                print("No transactions yet.")
            else:
                for i, j in enumerate(transactions, 1):
                    print(f"{i}. Withdrawn: ₦{j['withdrawn']:.2f}, Fee: ₦{j['fee']}, Balance: ₦{j['balance']:.2f}")

        elif choice == '3':
            print("Thank you for using the SEMICOLON AFRICA ATM. Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1, 2, or 3.")


atm_system()
