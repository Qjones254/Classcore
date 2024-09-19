from rich.console import Console
from parents import view_children
from pupils import students_menu

console=Console()
'''import sqlite3

CONN = sqlite3.connect('classcore.db')
CURSOR = CONN.cursor()'''

from teachers import teacher_menu
from principal import principal_menu

def main():
    choice = 0
    while choice != 5:

        console.print(" Welcome to\n****CLASSCORE**** :book:",style="bold underline green")
        console.print("1) Teacher",style="blue")
        console.print("2) Student",style="blue")
        console.print("3) Parent",style="blue")
        console.print("4) Principal",style="blue")
        console.print("5) Exit",style="red")
        choice = int(input())

        if choice == 1:
            teacher_menu()
        elif choice == 2:
            students_menu()
        elif choice == 3:
            view_children()
        elif choice == 4:
            principal_menu()
        elif choice == 5:
            console.print("Exiting...")
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
