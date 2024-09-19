from teachers import view_students
from rich.console import Console
import sqlite3

console= Console()

def view_children():
    while True:
        console.print("1) View students",style='purple')
        console.print("2) Search student by name",style='purple')
        console.print("3) Exit",style='red')
        choice = int(input("Enter your choice: "))

        if choice == 1:
            view_students()
        elif choice == 2:
            search_student_by_name()
        elif choice == 3:
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

def search_student_by_name():
    name_to_search = input("Enter the name of the student to search: ")

    # Connect to the database
    conn = sqlite3.connect('school.db')  
    cursor = conn.cursor()
    
    # Query to search for the student by name
    cursor.execute("SELECT * FROM students WHERE first_name LIKE ?", ('%' + name_to_search + '%',))
    
    # Fetch all matching records
    found_students = cursor.fetchall()
    
    if found_students:
        print("Students found:")
        for student in found_students:
            id,grade_level,first_name,last_name,teacher,marks,grade = student
            console.print(f'ID:{id}\n Grade Level:{grade_level}\n Name:{first_name} {last_name}\n Teacher:{teacher}\n Marks:{marks}\n Grade:{grade}',style='green')
    else:
        print("No students found with that name.")
    
    # Close the connection
    conn.close()




