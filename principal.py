import sqlite3
from tabulate import tabulate

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

def add_teacher():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    grade_teaching = input("Enter grade teaching: ")
    pay_per_month = float(input("Enter pay per month: "))

    CONN = sqlite3.connect('school.db')
    cursor = CONN.cursor()

    cursor.execute('''
        INSERT INTO teachers (first_name, last_name, grade_teaching, pay_per_month)
        VALUES (?, ?, ?, ?)
    ''', (first_name, last_name, grade_teaching, pay_per_month))

    CONN.commit()
    CONN.close()
    print("Teacher added successfully.")

def view_teachers():
    CONN = sqlite3.connect('school.db')
    cursor = CONN.cursor()

    cursor.execute('SELECT * FROM teachers')
    teachers = cursor.fetchall()

    if not teachers:
        print("No teachers found.")
    else:
        headers = ["ID", "First Name", "Last Name", "Grade Teaching", "Pay per Month"]
        print(tabulate(teachers, headers=headers, tablefmt="grid"))

    CONN.close()

def principal_menu():
    while True:
        print("1) Add Teacher")
        print("2) View Teachers")
        print("3) Exit")
        choice = int(input())
        if choice == 1:
            add_teacher()
        elif choice == 2:
            view_teachers()
        elif choice == 3:
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    create_database()
    principal_menu()
