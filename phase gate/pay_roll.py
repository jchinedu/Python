employees = {}

def print_menu():
    print("Welcome to Semicolon Employees Payroll")
    print("====================================")
    print("1. Add employee payroll")
    print("2. View employees payroll")
    print("3. Update employee payroll")
    print("4. Exit")
    print("====================================")

def add_employee():
    name = input("Enter employee name: ").strip().lower()
    if name in employees:
        print(f"{name} already exists")
        return

    try:
        hours = float(input("Enter number of hours worked in a week: "))
        if hours > 40:
            print("oga oga oga you cant work for more than 40 hours.")
            return
    except ValueError:
        print("Invalid input for hours.")
        return

    try:
        rate = float(input("Enter hourly pay rate: "))
        federal = float(input("Enter federal tax withholding rate: "))
        state = float(input("Enter state tax withholding rate: "))
    except ValueError:
        print("Invalid numeric input.")
        return

    choice = input("Do you wish to continue or to go back? (c/b): ").lower()
    if choice == 'b':
        return

    employees[name] = {
        'hours': hours,
        'rate': rate,
        'federal': federal,
        'state': state
    }
    print("Employee payroll added.")

def view_employees():
    if not employees:
        print("No employee payroll to display.")
        return

    for name, data in employees.items():
        hours = data['hours']
        rate = data['rate']
        federal = data['federal']
        state = data['state']
        gross = hours * rate
        fed_withhold = gross * (federal / 100)
        state_withhold = gross * (state / 100)
        total_deduction = fed_withhold + state_withhold
        net_pay = gross - total_deduction

        print(f"\nEmployee Name: {name}")
        print(f"Hours Worked: {hours}")
        print(f"Pay Rate: ${rate:.2f}")
        print(f"Gross Pay: ${gross:.2f}")
        print("Deductions:")
        print(f"  Federal Withholding ({federal:.1f}%): ${fed_withhold:.2f}")
        print(f"  State Withholding ({state:.1f}%): ${state_withhold:.2f}")
        print(f"  Total Deduction: ${total_deduction:.2f}")
        print(f"Net Pay: ${net_pay:.2f}")

def update_employee():
    name = input("Enter employee name to update: ").lower()
    if name not in employees:
        print("Employee does not exist.")
        return

    try:
        hours = float(input("Enter new number of hours worked: "))
        if hours > 40:
            print("Error: Hours cannot exceed 40.")
            return
        rate = float(input("Enter new hourly pay rate: "))
        federal = float(input("Enter new federal tax withholding rate: "))
        state = float(input("Enter new state tax withholding rate: "))
    except ValueError:
        print("Invalid numeric input.")
        return

    employees[name]['hours'] = hours
    employees[name]['rate'] = rate
    employees[name]['federal'] = federal
    employees[name]['state'] = state
    print("Employee payroll updated.")

def main():
    while True:
        print_menu()
        choice = input("Enter the number you want to select: ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            update_employee()
        elif choice == '4':
            print("Exiting Payroll System...")
            break
        else:
            print("Invalid input. Try again.")

if __name__ == "__main__":
    main()
