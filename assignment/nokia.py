def wait_for_go_back():
    while True:
        try:
            user_input = int(input("Enter 0 to go back: "))
            if user_input == 0:
                break
            else:
                print("Only 0 is allowed to go back. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number (0).")

def phone_book():
    while True:
        message2 = """
===============================
       PhoneBook Menu
===============================
1  - Search
2  - Service Nos.
3  - Add name
4  - Erase
5  - Edit
6  - Assign tone
7  - Send b'card
8  - Option
9  - Speed dials
10 - Voice tags
0  - Enter 0 to go back to previous menu 
===============================
"""
        print(message2)
        try:
            number2 = int(input("Enter a number to select: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        match number2:
            case 0:
                return
            case 1:
                print("Search")
                wait_for_go_back()
            case 2:
                print("Service Nos.")
                wait_for_go_back()
            case 3:
                print("Add name")
                wait_for_go_back()
            case 4:
                print("Erase")
                wait_for_go_back()
            case 5:
                print("Edit")
                wait_for_go_back()
            case 6:
                print("Assign tone")
                wait_for_go_back()
            case 7:
                print("Send b'card")
                wait_for_go_back()
            case 8:
                while True:
                    message3 = """
==============================
         Options Menu
==============================
1 - Type of view
2 - Memory status
0 - Enter 0 to go back to the previous menu
==============================
"""
                    print(message3)
                    try:
                        num3 = int(input("Enter a number to select: "))
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                        continue

                    match num3:
                        case 0:
                            break
                        case 1:
                            print("Type of view")
                            wait_for_go_back()
                        case 2:
                            print("Memory status")
                            wait_for_go_back()
                        case _:
                            print("Invalid input. Please try again.")

            case 9:
                print("Speed dials")
                wait_for_go_back()
            case 10:
                print("Voice tags")
                wait_for_go_back()
            case _:
                print("Invalid input. Please try again.")

def messages():
    while True:
        message3 = """
===============================
        Messaging Menu
===============================
1  - Write messages
2  - Inbox
3  - Outbox
4  - Picture messages
5  - Templates
6  - Smileys
7  - Message settings
8  - Info service
9  - Voice mailbox number
10 - Service command editor
0  - Enter 0 to go back to previous menu
===============================
"""
        print(message3)
        try:
            number3 = int(input("Enter a number to select: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        match number3:
            case 0:
                return
            case 1:
                print("Write messages:")
                wait_for_go_back()
            case 2:
                print("Inbox")
                wait_for_go_back()
            case 3:
                print("Outbox")
                wait_for_go_back()
            case 4:
                print("Picture messages")
                wait_for_go_back()
            case 5:
                print("Templates")
                wait_for_go_back()
            case 6:
                print("Smileys")
                wait_for_go_back()
            case 7:
                while True:
                    message31 = """
===============================
      Message Settings Menu
===============================
1 - Set 1
2 - Common
0 - Enter 0 to go back to previous menu
===============================
"""
                    print(message31)
                    try:
                        number31 = int(input("Enter a number to select: "))
                    except ValueError:
                        print("Invalid input.")
                        continue

                    match number31:
                        case 0:
                            break
                        case 1:
                            while True:
                                message32 = """
===============================
    Message Settings (SET 1)
===============================
1. Message center number
2. Message sent as
3. Message validity
0. Enter 0 to go back to previous menu
===============================
"""
                                print(message32)
                                try:
                                    number32 = int(input("Enter a number to select: "))
                                except ValueError:
                                    print("Invalid input.")
                                    continue

                                match number32:
                                    case 0:
                                        break
                                    case 1:
                                        print("Message center number")
                                        wait_for_go_back()
                                    case 2:
                                        print("Messages sent as")
                                        wait_for_go_back()
                                    case 3:
                                        print("Message validity")
                                        wait_for_go_back()
                                    case _:
                                        print("Invalid input.")
                        case 2:
                            while True:
                                print("""
===============================
  Common Message Settings
===============================
1. Delivery reports
2. Reply via same centre
3. Character support
0. Go back
===============================
""")
                                try:
                                    number33 = int(input("Select an option: "))
                                except ValueError:
                                    print("Invalid input.")
                                    continue

                                match number33:
                                    case 0:
                                        break
                                    case 1:
                                        print("Delivery reports")
                                        wait_for_go_back()
                                    case 2:
                                        print("Reply via same centre")
                                        wait_for_go_back()
                                    case 3:
                                        print("Character support")
                                        wait_for_go_back()
                                    case _:
                                        print("Invalid input.")
                        case _:
                            print("Invalid input.")
            case 8:
                print("Info service")
                wait_for_go_back()
            case 9:
                print("Voice mailbox number")
                wait_for_go_back()
            case 10:
                print("Service command editor")
                wait_for_go_back()
            case _:
                print("Invalid input")
                wait_for_go_back()

def chat():
    while True:
        print("""
===================================
Chat with friends and connect with 
people all over the world!
===================================
Enter 0 to go back to Main Menu.
""")
        try:
            choice = int(input("Enter a number to select: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        match choice:
            case 0:
                break
            case _:
                print("Invalid choice. Enter 0 to go back.")

def call_register():
    while True:
        message34 = """
===============================
        Call Register Menu
===============================
1 - Missed call
2 - Received call
3 - Dialled numbers
4 - Erase recent call lists
5 - Show call duration
6 - Show call cost
7 - Call cost settings
8 - Prepaid credit
0 - Enter 0 to go back to previous menu
===============================
"""
        print(message34)
        try:
            number34 = int(input("Enter a number to select: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        match number34:
            case 0:
                return
            case 1:
                print("Missed call")
                wait_for_go_back()
            case 2:
                print("Received call")
                wait_for_go_back()
            case 3:
                print("Dialled numbers")
                wait_for_go_back()
            case 4:
                print("Erase recent call lists")
                wait_for_go_back()
            case 5:
                while True:
                    message35 = """
===============================
       Call Duration Menu
===============================
1 - Last call duration
2 - All calls duration
3 - Received calls duration
4 - Dialled calls duration
5 - Clear timers
0 - Enter 0 to go back to previous menu
===============================
"""
                    print(message35)
                    try:
                        number35 = int(input("Enter a number to select: "))
                    except ValueError:
                        print("Invalid input.")
                        continue

                    match number35:
                        case 0:
                            break
                        case 1:
                            print("Last call duration")
                            wait_for_go_back()
                        case 2:
                            print("All calls duration")
                            wait_for_go_back()
                        case 3:
                            print("Received calls duration")
                            wait_for_go_back()
                        case 4:
                            print("Dialled calls duration")
                            wait_for_go_back()
                        case 5:
                            print("Clear timers")
                            wait_for_go_back()
                        case _:
                            print("Invalid input")
            case 6:
                while True:
                    message36 = """
===============================
        Show Call Cost Menu
===============================
1 - Last call cost
2 - All calls cost
3 - Clear counters
0 - Enter 0 to go back to previous menu
===============================
"""
                    print(message36)
                    try:
                        number36 = int(input("Enter a number to select: "))
                    except ValueError:
                        print("Invalid input.")
                        continue

                    match number36:
                        case 0:
                            break
                        case 1:
                            print("Last call cost")
                            wait_for_go_back()
                        case 2:
                            print("All calls cost")
                            wait_for_go_back()
                        case 3:
                            print("Clear counters")
                            wait_for_go_back()
                        case _:
                            print("Invalid input")
            case 7:
                while True:
                    message37 = """
===============================
      Call Cost Settings
===============================
1 - Call cost limit
2 - Show cost in
0 - Enter 0 to go back to previous menu
===============================
"""
                    print(message37)
                    try:
                        number37 = int(input("Enter a number to select: "))
                    except ValueError:
                        print("Invalid input.")
                        continue

                    match number37:
                        case 0:
                            break
                        case 1:
                            print("Call cost limit")
                            wait_for_go_back()
                        case 2:
                            print("Show cost in")
                            wait_for_go_back()
                        case _:
                            print("Invalid input")
            case 8:
                print("Prepaid credit")
                wait_for_go_back()
            case _:
                print("Invalid input")
def tones():
    while True:
        message38 = """
===============================
       Tones Settings Menu
===============================
1 - Ringing tone
2 - Ringing volume
3 - Incoming call alert
4 - Composer
5 - Message alert tone
6 - Keypad tones
7 - Warning and game tones
8 - Vibrating alert
9 - Screen saver
0 - Enter 0 to go back to previous menu
===============================
"""
        print(message38)

        try:
            number38 = int(input("Enter a number to select: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        match number38:
            case 0:
                return
            case 1:
                print("Ringing tone")
                wait_for_go_back()
            case 2:
                print("Ringing volume")
                wait_for_go_back()
            case 3:
                print("Incoming call alert")
                wait_for_go_back()
            case 4:
                print("Composer")
                wait_for_go_back()
            case 5:
                print("Message alert tone")
                wait_for_go_back()
            case 6:
                print("Keypad tones")
                wait_for_go_back()
            case 7:
                print("Warning and game tones")
                wait_for_go_back()
            case 8:
                print("Vibrating alert")
                wait_for_go_back()
            case 9:
                print("Screen saver")
                wait_for_go_back()
            case _:
                print("Invalid input. Please try again.")

def settings():
    while True:
        message39 = """
===============================
         Settings Menu
===============================
1 - Call settings
2 - Phone settings
3 - Security settings
4 - Restore factory settings
0 - Enter 0 to go back to previous menu
===============================
"""
        print(message39)

        try:
            number39 = int(input("Enter a number to select: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        match number39:
            case 0:
                return

            case 1:
                while True:
                    message40 = """
===============================
         Call Settings
===============================
1 - Automatic redial
2 - Speed dialing
3 - Call waiting options
4 - Own number sending
5 - Phone line in use
6 - Automatic answer
0 - Enter 0 to go back to previous menu
===============================
"""
                    print(message40)
                    try:
                        number40 = int(input("Enter a number to select: "))
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                        continue

                    match number40:
                        case 0:
                            break
                        case 1:
                            print("Automatic redial")
                            wait_for_go_back()
                        case 2:
                            print("Speed dialing")
                            wait_for_go_back()
                        case 3:
                            print("Call waiting options")
                            wait_for_go_back()
                        case 4:
                            print("Own number sending")
                            wait_for_go_back()
                        case 5:
                            print("Phone line in use")
                            wait_for_go_back()
                        case 6:
                            print("Automatic answer")
                            wait_for_go_back()
                        case _:
                            print("Invalid input")

            case 2:
                while True:
                    message01 = """
===============================
        Phone Settings
===============================
1 - Language
2 - Cell info display
3 - Welcome note
4 - Network selection
5 - Lights
6 - Confirm SIM service action
0 - Enter 0 to go back to previous menu
===============================
"""
                    print(message01)
                    try:
                        number43 = int(input("Enter a number to select: "))
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                        continue

                    match number43:
                        case 0:
                            break
                        case 1:
                            print("Language")
                            wait_for_go_back()
                        case 2:
                            print("Cell info display")
                            wait_for_go_back()
                        case 3:
                            print("Welcome note")
                            wait_for_go_back()
                        case 4:
                            print("Network selection")
                            wait_for_go_back()
                        case 5:
                            print("Lights")
                            wait_for_go_back()
                        case 6:
                            print("Confirm SIM service action")
                            wait_for_go_back()
                        case _:
                            print("Invalid input")

            case 3:
                while True:
                    message42 = """
===============================
     Security Settings
===============================
1 - Pin code request
2 - Call barring service
3 - Fixed dialing
4 - Closed user group
5 - Phone security
6 - Change access codes
0 - Enter 0 to go back to previous menu
===============================
"""
                    print(message42)
                    try:
                        number41 = int(input("Enter a number to select: "))
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                        continue

                    match number41:
                        case 0:
                            break
                        case 1:
                            print("Pin code request")
                            wait_for_go_back()
                        case 2:
                            print("Call barring service")
                            wait_for_go_back()
                        case 3:
                            print("Fixed dialing")
                            wait_for_go_back()
                        case 4:
                            print("Closed user group")
                            wait_for_go_back()
                        case 5:
                            print("Phone security")
                            wait_for_go_back()
                        case 6:
                            print("Change access codes")
                            wait_for_go_back()
                        case _:
                            print("Invalid input")

            case 4:
                print("Restore Factory Settings")
                wait_for_go_back()

            case _:
                print("Invalid input")
def call_divert():
    while True:
        print("Call Divert")
        wait_for_go_back()
        break

def games():
    while True:
        print("Games")
        wait_for_go_back()
        break

def calculator():
    while True:
        print("Calculator")
        wait_for_go_back()
        break

def reminders():
    while True:
        print("Reminders")
        wait_for_go_back()
        break

def clock():
    while True:
        message44 = """
===============================
           CLOCK MENU
===============================
1 - Alarm clock
2 - Clock settings
3 - Date setting
4 - Stopwatch
5 - Countdown timer
6 - Auto update of date and time
0 - Enter 0 to go back to previous menu
===============================
"""
        print(message44)
        try:
            number44 = int(input("Enter a number to select: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        match number44:
            case 0:
                return
            case 1:
                print("Alarm clock")
                wait_for_go_back()
            case 2:
                print("Clock settings")
                wait_for_go_back()
            case 3:
                print("Date setting")
                wait_for_go_back()
            case 4:
                print("Stopwatch")
                wait_for_go_back()
            case 5:
                print("Countdown timer")
                wait_for_go_back()
            case 6:
                print("Auto update of date and time")
                wait_for_go_back()
            case _:
                print("Invalid input")

def profiles():
    while True:
        print("Profiles")
        wait_for_go_back()
        break
def sim_service():
    while True:
        print("Sim services")
        wait_for_go_back()
        break
while True:
    message = """
===========================
  NOKIA 3310 - MAIN MENU 
===========================
1 - Phone Book
2 - Messages
3 - Chat
4 - Call Register
5 - Tones
6 - Settings
7 - Call Divert
8 - Games
9 - Calculator
10 - Reminders
11 - Clock
12 - Profiles
13 - Sim Service
0  - Exit
===========================
"""
    print(message)
    choice = input("Enter a number to select: ")

    try:
        number = int(choice)
    except ValueError:
        print("Invalid input: please enter a number.")
        continue

    match number:
        case 1:
            phone_book()
        case 2:
            messages()
        case 3:
            chat()
        case 4:
            call_register()
        case 5:
            tones()
        case 6:
            settings()
        case 7:
            call_divert()
        case 8:
            games()
        case 9:
            calculator()
        case 10:
            reminders()
        case 11:
            clock()
        case 12:
            profiles()
        case 13:
            sim_service()
        case 0:
            print("NOKIA....BYE!")
            break
        case _:
            print("Invalid input")
