import sqlite3
from rich.console import Console

console=Console()

def create_database():
    CONN = sqlite3.connect('school.db')
    cursor = CONN.cursor()

    # Creating teachers table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS teachers(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            grade_teaching TEXT,
            pay_per_month REAL     
        )
    ''')
    CONN.commit()
    CONN.close()
    print("Database and tables created successfully.")

#This function helps the principal know the number of teachers to ensure they do not pass the maximum 
def get_teacher_count():
    CONN = sqlite3.connect('school.db')
    cursor = CONN.cursor()
    
    cursor.execute('SELECT COUNT(*) FROM teachers')
    count = cursor.fetchone()[0]

    CONN.close()
    return count

def add_teacher():
    current_count = get_teacher_count()
    #The principal cannot add more than 9 teachers since there are 9 grades
    if current_count >= 9:
        print("Maximum number of teachers (9) already added. Cannot add more.")
        return

    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    grade_teaching = input("Enter grade teaching: ")
    pay_per_month = float(input("Enter pay per month: "))
    #This adds the teacher to the database
    CONN = sqlite3.connect('school.db')
    cursor = CONN.cursor()

    cursor.execute('''
        INSERT INTO teachers (first_name, last_name, grade_teaching, pay_per_month)
        VALUES (?, ?, ?, ?)
    ''', (first_name, last_name, grade_teaching, pay_per_month))

    CONN.commit()
    CONN.close()
    console.print("Teacher added successfully.",style='green')

def view_teachers():
    CONN = sqlite3.connect('school.db')
    cursor = CONN.cursor()

    cursor.execute('SELECT * FROM teachers')
    teachers = cursor.fetchall()

    if not teachers:
        console.print("No teachers found.",style='red')
    else:
        print(f"{'ID':<5} {'First Name':<15} {'Last Name':<15} {'Grade Teaching':<15} {'Pay per Month':<15}")
        print("=" * 70)
        for teacher in teachers:
            #The angles represent the space between rows in the table for well arranged work
            print(f"{teacher[0]:<5} {teacher[1]:<15} {teacher[2]:<15} {teacher[3]:<15} {teacher[4]:<15}")

    CONN.close()

def remove_teacher():
    #The user views the teachers first to know which ID to remove
    view_teachers()
    #We remove the teacher from the database with their ID
    teacher_id = int(input("Enter the ID of the teacher you want to remove: "))

    CONN = sqlite3.connect('school.db')
    cursor = CONN.cursor()

    cursor.execute('DELETE FROM teachers WHERE id = ?', (teacher_id,))
    #Printing an error if the ID input is not in the table
    if cursor.rowcount == 0:
        print(f"No teacher found with ID {teacher_id}.")
    else:
        console.print("Teacher removed successfully.",style='red')

    CONN.commit()
    CONN.close()

def principal_menu():
    while True:
        password = "manager"
        password = input("Enter password: ")
        if password !="manager":
            console.print("Invalid password.Please enter a valid password",style='red')
        else:
         console.print("1) Add Teacher",style='purple')
         console.print("2) View Teachers",style='purple')
         console.print("3) Remove Teacher",style='purple')
         console.print("4) Exit",style='red')
         choice = int(input())
         if choice == 1:
            add_teacher()
         elif choice == 2:
            view_teachers()
         elif choice == 3:
            remove_teacher()
         elif choice == 4:
            break
         else:
            console.print("Invalid choice. Try again.",style='red')

if __name__ == "__main__":
    create_database()
    principal_menu()
