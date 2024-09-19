from teachers import view_students

def view_children():
    while True:
        print("1) View students")
        print("2) Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            view_students()
        elif choice == 2:
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")


