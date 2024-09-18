# main.py
'''import sqlite3

CONN = sqlite3.connect('classcore.db')
CURSOR = CONN.cursor()'''

from teachers import teacher_menu
from principal import principal_menu

def main():
    choice = 0
    while choice != 5:

        print("Welcome to\n****CLASSCORE****")
        print("1) Teacher")
        print("2) Student")
        print("3) Parent")
        print("4) Principal")
        print("5) Exit")
        choice = int(input())

        if choice == 1:
            teacher_menu()
        elif choice == 2:
            print("Student functionality is not implemented yet.")
        elif choice == 3:
            print("Parent functionality is not implemented yet.")
        elif choice == 4:
            principal_menu()
        elif choice == 5:
            print("Exiting...")
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
