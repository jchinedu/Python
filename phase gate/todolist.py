Tasks = []
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
def add_a_task():
 while True:
  message2 = """
===============================
       ADD A TASK
===============================
1  - ADD
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
     add = input('enter what you want to add')
     task={}
     Tasks.append(task)
     print("task added")
     wait_for_go_back()
    case _:
     print("Invalid input. Please try again.")
def view_task():
 while True:
  message2 = """
===============================
       TASK VIEWER
===============================
1  - view task
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
     Tasks = ([] buy_groceries [] finish_homeworks)
     print(Tasks)
     wait_for_go_back()
    case _:
     print("Invalid input. Please try again.")

while True:
    message = """
===========================
   TO DO LIST MAIN MENU 
===========================
1 - Add a task
2 - View tasks
3 - Mark a task as complete
4 - Delete a task
0 - Exit
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
            add_a_task()
        case 2:
            view_task()
        case 3:
            mark_a_task_as_complete()
        case 4:
            Delete_a_task()
        case 0:
            print("...BYE!...")
            break 
        case _:
            print("Invalid input")
