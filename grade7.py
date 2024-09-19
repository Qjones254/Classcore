import sqlite3
from tabulate import tabulate

def get_grade7_table():
    # Connecting to the database
    CONN = sqlite3.connect('school.db')
    cursor = CONN.cursor()
    # Creating students table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS grade7(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            teacher TEXT,
            marks REAL,
            grade TEXT       
        )
    ''')
    CONN.commit()
    print("Grade7 Students table added successfully!")
    CONN.close()
###############################################################################################
def view_grade_students():
    CONN = sqlite3.connect('school.db')
    cursor = CONN.cursor()

    cursor.execute('SELECT * FROM grade7')
    students = cursor.fetchall()

    if not students:
        print("No students found!")
    else:
        headers =['ID','first_name','last_name','teacher','marks','grade']
        print(tabulate(students,headers=headers,tablefmt='pretty'))

############################################################################################################
def insert_student(first_name, last_name, teacher, marks, grade):
    # Connecting to the database
    CONN = sqlite3.connect('school.db')  
    cursor = CONN.cursor()  
    # Insert a new student
    cursor.execute('''
       INSERT INTO grade7(first_name, last_name, teacher, marks, grade)
       VALUES(?,?,?,?,?)
    ''', (first_name, last_name, teacher, marks, grade))

    CONN.commit()
    print(f"Student {first_name} {last_name} added successfully")
    CONN.close()

def populate_students():
    # Connecting to the database
    CONN = sqlite3.connect('school.db')  
    cursor = CONN.cursor()
    
    # Check if the table is empty
    cursor.execute('SELECT COUNT(*) FROM grade7')
    count = cursor.fetchone()[0]

    if count == 0:
        # Insert students only if the table is empty
        students = [
            ('Mercy', 'Wanjiru', 'Jean Mwangi', 80.2, 'B'),
            ('Prudence', 'Onjiri', 'Jean Mwangi', 96.4, 'A'),
            ('Jean', 'Musaka', 'Jean Mwangi', 74.0, 'B'),
            ('King', 'Kimani', 'Jean Mwangi', 67.2, 'C'),
            ('Ferdinand', 'Otwiri', 'Jean Mwangi', 94.2, 'A'),
            ('Ellana', 'Mwiri', 'Jean Mwangi', 4.2, 'F'),
            ('Angel', 'Mumbi', 'Jean Mwangi', 90.0, 'A'),
            ('Georgina', 'Musaku', 'Jean Mwangi', 76.7, 'B'),
            ('Pendo', 'Waithers', 'Jean Mwangi', 55.5, 'C'),
            ('Pony', 'Angel', 'Jean Mwangi', 97.3, 'A')
        ]

        for student in students:
            insert_student(*student)
    else:
        print("Students already exist in the database.")
    
    CONN.close()
######################################################################################################
def update_student_grade(student_id, new_marks, new_grade):
    # Connecting to the database
    CONN = sqlite3.connect('school.db')  
    cursor = CONN.cursor()
    
    # Update the student's marks and grade
    cursor.execute('''
        UPDATE grade7
        SET marks = ?, grade = ?
        WHERE id = ?
    ''', (new_marks, new_grade, student_id))
    
    # Commit changes
    CONN.commit()
    
    if cursor.rowcount == 0:
        print("No student found with that ID.")
    else:
        print(f"Student ID {student_id} updated successfully.")
    
    CONN.close()
#############################################################################################
def change_student_grades():
    try:
        student_id = int(input("Enter the Student ID to update: "))
        new_marks = float(input("Enter the new marks: "))
        new_grade = input("Enter the new grade: ")

        update_student_grade(student_id, new_marks, new_grade)
    except ValueError:
        print("Invalid input. Please enter numeric values for ID and marks.")
######################################################################################################
if __name__ == '__main__':
    get_grade7_table()
    populate_students()
