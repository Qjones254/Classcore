from rich.console import Console
from parents import view_children
from pupils import students_menu
#This is for a pretty output it is activated by adding console to every print
console=Console()

from teachers import teacher_menu
from principal import principal_menu
#This function is for the main menu
def main():
    choice = 0
    while choice != 5:

        console.print(" Welcome to\n:book:************:book:\n    CLASSCORE\n:book:*********** :book:",style="bold  green")
        console.print("1) Teacher",style="blue")
        console.print("2) Student",style="blue")
        console.print("3) Parent",style="blue")
        console.print("4) Principal",style="blue")
        console.print("5) Exit",style="red")
        choice = int(input())
       #Imported function from teachers.py
        if choice == 1:
            teacher_menu()
            #Imported function from pupils.py
        elif choice == 2:
            students_menu()
            #Imported function from parents.py
        elif choice == 3:
            view_children()
            #Imported function from princial.py
        elif choice == 4:
            principal_menu()
        elif choice == 5:
            console.print("Exiting...")
            
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
