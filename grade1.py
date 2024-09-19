import sqlite3
from tabulate import tabulate

def get_grade1_table():
    # Connecting to the database
    CONN = sqlite3.connect('school.db')
    cursor = CONN.cursor()
    # Creating students table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS grade1(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            teacher TEXT,
            marks REAL,
            grade TEXT       
        )
    ''')
    CONN.commit()
    print("Grade1 Students table added successfully!")
    CONN.close()
#####################################################################################################
def insert_student(first_name, last_name, teacher, marks, grade):
    # Connecting to the database
    CONN = sqlite3.connect('school.db')  
    cursor = CONN.cursor()  
    # Insert a new student
    cursor.execute('''
       INSERT INTO grade1(first_name, last_name, teacher, marks, grade)
       VALUES(?,?,?,?,?)
    ''', (first_name, last_name, teacher, marks, grade))

    CONN.commit()
    print(f"Student {first_name} {last_name} added successfully")
    CONN.close()
##########################################################################################################
def view_grade_students():
    CONN = sqlite3.connect('school.db')
    cursor = CONN.cursor()

    cursor.execute('SELECT * FROM grade1')
    students = cursor.fetchall()

    if not students:
        print("No students found!")
    else:
        headers =['ID','first_name','last_name','teacher','marks','grade']
        print(tabulate(students,headers=headers,tablefmt='pretty'))
###################################################################################################
def populate_students():
    # Connecting to the database
    CONN = sqlite3.connect('school.db')  
    cursor = CONN.cursor()
    
    # Check if the table is empty
    cursor.execute('SELECT COUNT(*) FROM grade1')
    count = cursor.fetchone()[0]

    if count == 0:
        # Insert students only if the table is empty
        students = [
            ('John', 'Kiriamiti', 'Quincy Mwangi', 80.2, 'B'),
            ('Max', 'Steppan', 'Quincy Mwangi', 86.4, 'B'),
            ('Jim', 'Ludacris', 'Quincy Mwangi', 94.0, 'A'),
            ('Leon', 'Kimani', 'Quincy Mwangi', 60.2, 'C'),
            ('Ferdinand', 'Omanyala', 'Quincy Mwangi', 66.2, 'C'),
            ('Erick', 'Mbuthia', 'Quincy Mwangi', 95.2, 'A'),
            ('Collins', 'Mucheru', 'Quincy Mwangi', 40.0, 'D'),
            ('Henry', 'Musaku', 'Quincy Mwangi', 76.7, 'B'),
            ('Caleb', 'Lintir', 'Quincy Mwangi', 55.5, 'D'),
            ('Ian', 'George', 'Quincy Mwangi', 87.3, 'B')
        ]

        for student in students:
            insert_student(*student)
    else:
        print("Students already exist in the database.")
    
    CONN.close()
###########################################################################
def update_student_grade(student_id, new_marks, new_grade):
    # Connecting to the database
    CONN = sqlite3.connect('school.db')  
    cursor = CONN.cursor()
    
    # Update the student's marks and grade
    cursor.execute('''
        UPDATE grade1
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
##############################################################################################################
def change_student_grades():
    try:
        student_id = int(input("Enter the Student ID to update: "))
        new_marks = float(input("Enter the new marks: "))
        new_grade = input("Enter the new grade: ")

        update_student_grade(student_id, new_marks, new_grade)
    except ValueError:
        print("Invalid input. Please enter numeric values for ID and marks.")



if __name__ == '__main__':
    get_grade1_table()
    populate_students()
