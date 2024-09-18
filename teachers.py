# teachers.py


def authenticate_teacher():
    name = input("Enter your name >>> ")
    print(f"Welcome {name}")
    password = input("Enter password: ")
    if password != "Admin":
        print("Enter a valid password!")
        return None
    return name

def teacher_menu():
    name = authenticate_teacher()
    if name:
        while True:
            print("1) Mark Students' grades")
            print("2) View Students' grades")
            print("3) Exit")
            choice = int(input())
            if choice == 1:
                mark_grades()
            elif choice == 2:
                # Add functionality to view students' grades
                print("Function not applied yet")
            elif choice == 3:
                break
            else:
                print("Invalid choice. Try again.")

def mark_grades():
    while True:
        print("What grade do you teach?")
        print("1) Grade 1")
        print("2) Grade 2")
        print("3) Grade 3")
        print("4) Grade 4")
        print("5) Grade 5")
        print("6) Exit.")
        choice = int(input())
        if choice == 6:
            break
        if 1 <= choice <= 5:
            password = input(f"Enter grade{choice} password: ")
            if password == f"grade{choice}":
                while True:
                    print("Welcome")
                    print("Choose an option")
                    print("1) View students' grades")
                    print("2) Exit")
                    option = int(input())
                    if option == 2:
                        break
            else:
                print(f"Enter a valid password for grade{choice}!")
        else:
            print("Invalid choice. Try again.")


