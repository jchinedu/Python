from datetime import datetime, timedelta, date
import random

def main():
    def print_welcome_banner():
        print("==================================")
        print("   Welcome to Semi Flow Tracker   ")
        print("==================================")

    def print_main_menu():
        print("\nAre you using Semi Flow for yourself?")
        print("1. Yes")
        print("2. No, I have a partner")
        print("0. Exit")

    def get_int_input(prompt, valid_options=None):
        while True:
            try:
                choice = int(input(prompt))
                if valid_options and choice not in valid_options:
                    print(f"Please enter one of these: {valid_options}")
                    continue
                return choice
            except ValueError:
                print("Invalid input. Please enter a number.")

    def handle_personal_use():
        discovery_sources = [
            "Semicolon Africa",
            "Personal learning",
            "Friends or family",
            "Google Play or Google Search",
            "TikTok",
            "YouTube",
            "Influencer or Celebrity",
            "Medical professional",
            "Others"
        ]
        print("\nHow did you find out about Semi Flow?")
        for idx, source in enumerate(discovery_sources, start=1):
            print(f"{idx}. {source}")

        source_choice = get_int_input("Enter your choice (1 to 9): ", range(1, 10))
        responses = {
            1: "Nice! Shoutout to Semicolon Africa.",
            2: "Learning is power!",
            3: "We're happy your circle shared us!",
            4: "Glad you searched and found us!",
            5: "TikTok knows everything!",
            6: "Thanks for watching and joining.",
            7: "Shoutout to the influencers out there!",
            8: "Great to know professionals recommend us.",
            9: "Thank you for discovering Semi Flow."
        }
        print(responses.get(source_choice, "Thanks for joining us!"))

        dob_input = input("\nWhen were you born? (Enter as YYYY-MM-DD): ")
        try:
            dob = datetime.strptime(dob_input, "%Y-%m-%d").date()
            age = (date.today() - dob).days // 365
            if age < 13:
                print("Sorry, Semi Flow is for users aged 13 and above.")
                return

            print("\nWelcome to Semi Flow!")
            print("Are you pregnant?")
            print("1. No, but I want to be")
            print("2. No, I am here to understand my body better")
            print("3. Yes, I am")

            pregnancy_choice = get_int_input("Enter your choice: ", {1, 2, 3})
            if pregnancy_choice == 1:
                print("We’re here to support your journey.")
            elif pregnancy_choice == 2:
                print("Awesome! Let's help you understand your body better.")
                get_menstrual_cycle_input()
            elif pregnancy_choice == 3:
                print("Congratulations! Pregnancy support features coming soon.")
            else:
                print("Thanks for sharing!")

        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    print_welcome_banner()

    while True:
        print_main_menu()
        main_choice = get_int_input("Enter your choice: ", {0, 1, 2})

        if main_choice == 1:
            handle_personal_use()
        elif main_choice == 2:
            print("Partner tracking isn’t available yet. Press 0 to return to the main menu.")
        elif main_choice == 0:
            print("Thank you for using Semi Flow. Goodbye!")
            break

# ========== Menstrual Tracking Functions ==========

def get_menstrual_cycle_input():
    while True:
        try:
            name = input("What is your name? ")
            date_input = input("Enter the first day of your last menstrual cycle (YYYY-MM-DD): ")
            start_date = datetime.strptime(date_input, "%Y-%m-%d").date()

            print(f"\nHello {name}, your last menstrual cycle started on {start_date.strftime('%d-%m-%Y')}.\n")

            print_period_flow_dates(start_date)
            print_ovulation_period(start_date)
            print_next_period_date(start_date)
            print_safe_period(start_date)

            break
        except ValueError:
            print("Invalid date, kindly enter the correct date in YYYY-MM-DD format.\n")

def print_period_flow_dates(start_date):
    print("Your Period flow dates (5 Days):")
    for i in range(5):
        day = start_date + timedelta(days=i)
        print(f"Day {i + 1}: {day.strftime('%d-%m-%Y')}")
    print()

def print_ovulation_period(start_date):
    ovulation_start = start_date + timedelta(days=12)
    ovulation_end = start_date + timedelta(days=16)
    print("Ovulation Period:")
    print(f"Start: {ovulation_start.strftime('%d-%m-%Y')}")
    print(f"End:   {ovulation_end.strftime('%d-%m-%Y')}")
    print()

def print_next_period_date(start_date):
    days_until_next = 28 + random.randint(0, 2)
    next_period = start_date + timedelta(days=days_until_next)
    print("Your Next Period Prediction:")
    print(f"Predicted Date: {next_period.strftime('%d-%m-%Y')}")
    print()

def print_safe_period(start_date):
    print("Safe Period Dates:")

    print("Before fertile window:")
    for i in range(12):
        safe_day = start_date + timedelta(days=i)
        print(safe_day.strftime('%d-%m-%Y'))

    print("\nAfter fertile window:")
    for i in range(19, 29):
        safe_day = start_date + timedelta(days=i)
        print(safe_day.strftime('%d-%m-%Y'))
    print()

# Run the program
if __name__ == "__main__":
    main()
