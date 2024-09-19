import sqlite3
from tabulate import tabulate

def get_grade4_table():
    # Connecting to the database
    CONN = sqlite3.connect('school.db')
    cursor = CONN.cursor()
    # Creating students table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS grade4(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            teacher TEXT,
            marks REAL,
            grade TEXT       
        )
    ''')
    CONN.commit()
    print("Grade4 Students table added successfully!")
    CONN.close()
###################################################################################################
def insert_student(first_name, last_name, teacher, marks, grade):
    # Connecting to the database
    CONN = sqlite3.connect('school.db')  
    cursor = CONN.cursor()  
    # Insert a new student
    cursor.execute('''
       INSERT INTO grade4(first_name, last_name, teacher, marks, grade)
       VALUES(?,?,?,?,?)
    ''', (first_name, last_name, teacher, marks, grade))

    CONN.commit()
    print(f"Student {first_name} {last_name} added successfully")
    CONN.close()
########################################################################################################3
def view_grade_students():
    CONN = sqlite3.connect('school.db')
    cursor = CONN.cursor()

    cursor.execute('SELECT * FROM grade4')
    students = cursor.fetchall()

    if not students:
        print("No students found!")
    else:
        headers =['ID','first_name','last_name','teacher','marks','grade']
        print(tabulate(students,headers=headers,tablefmt='pretty'))

############################################################################################################
def populate_students():
    # Connecting to the database
    CONN = sqlite3.connect('school.db')  
    cursor = CONN.cursor()
    
    # Check if the table is empty
    cursor.execute('SELECT COUNT(*) FROM grade4')
    count = cursor.fetchone()[0]

    if count == 0:
        # Insert students only if the table is empty
        students = [
            ('Ivy', 'Naisula', 'Peter Mbuthia', 0, 'F'),
            ('Gwen', 'Stacy', 'Peter Mbuthia', 96.4, 'A'),
            ('Barry', 'Allen', 'Peter Mbuthia', 54.0, 'D'),
            ('Jim', 'Carret', 'Peter Mbuthia', 80.2, 'B'),
            ('Brendan', 'Gwer', 'Peter Mbuthia', 76.2, 'B'),
            ('Emmiliana', 'Wambui', 'Peter Mbuthia', 0, 'F'),
            ('Mary', 'Jane', 'Peter Mbuthia', 40.0, 'D'),
            ('Hllen', 'Degener', 'Peter Mbuthia', 95.7, 'A'),
            ('Brianna', 'Njeri', 'Peter Mbuthia', 25.5, 'E'),
            ('Levy', 'Gilan', 'Peter Mbuthia', 87.3, 'B')
        ]

        for student in students:
            insert_student(*student)
    else:
        print("Students already exist in the database.")
    
    CONN.close()
    ######################################################################################
def update_student_grade(student_id, new_marks, new_grade):
    # Connecting to the database
    CONN = sqlite3.connect('school.db')  
    cursor = CONN.cursor()
    
    # Update the student's marks and grade
    cursor.execute('''
        UPDATE grade4
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
########################################################################################
def change_student_grades():
    try:
        student_id = int(input("Enter the Student ID to update: "))
        new_marks = float(input("Enter the new marks: "))
        new_grade = input("Enter the new grade: ")

        update_student_grade(student_id, new_marks, new_grade)
    except ValueError:
        print("Invalid input. Please enter numeric values for ID and marks.")

if __name__ == '__main__':
    get_grade4_table()
    populate_students()
