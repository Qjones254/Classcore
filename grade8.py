import sqlite3
from tabulate import tabulate
####################################################################################
def get_grade8_table():
    # Connecting to the database
    CONN = sqlite3.connect('school.db')
    cursor = CONN.cursor()
    # Creating students table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS grade8(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            teacher TEXT,
            marks REAL,
            grade TEXT       
        )
    ''')
    CONN.commit()
    print("Grade8 Students table added successfully!")
    CONN.close()
#############################################################################################3
def view_grade_students():
    CONN = sqlite3.connect('school.db')
    cursor = CONN.cursor()

    cursor.execute('SELECT * FROM grade8')
    students = cursor.fetchall()

    if not students:
        print("No students found!")
    else:
        headers =['ID','first_name','last_name','teacher','marks','grade']
        print(tabulate(students,headers=headers,tablefmt='pretty'))

####################################################################################################
def insert_student(first_name, last_name, teacher, marks, grade):
    # Connecting to the database
    CONN = sqlite3.connect('school.db')  
    cursor = CONN.cursor()  
    # Insert a new student
    cursor.execute('''
       INSERT INTO grade8(first_name, last_name, teacher, marks, grade)
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
    cursor.execute('SELECT COUNT(*) FROM grade8')
    count = cursor.fetchone()[0]

    if count == 0:
        # Insert students only if the table is empty
        students = [
            ('John', 'Badi', '', 40.2, 'E'),
            ('Jakes', 'Kamoche', '',96.4, 'A'),
            ('July', 'Wanjeru', '', 84.0, 'B'),
            ('Lenny', 'Were', '', 70.2, 'C'),
            ('Felistus', 'Akpolo', '', 86.2, 'B'),
            ('Edisth', 'Leiyan', '', 65.2, 'C'),
            ('Lincoln', 'Imenja', '', 50.0, 'D'),
            ('Peris', 'Mwenje', '', 76.7, 'B'),
            ('Collins', 'Mwangi', '', 55.5, 'C'),
            ('Ilano', 'Chirchir', '', 87.3, 'B')
        ]

        for student in students:
            insert_student(*student)
    else:
        print("Students already exist in the database.")
    
    CONN.close()
################################################################################################################
def update_student_grade(student_id, new_marks, new_grade):
    # Connecting to the database
    CONN = sqlite3.connect('school.db')  
    cursor = CONN.cursor()
    
    # Update the student's marks and grade
    cursor.execute('''
        UPDATE grade8
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

def change_student_grades():
    try:
        student_id = int(input("Enter the Student ID to update: "))
        new_marks = float(input("Enter the new marks: "))
        new_grade = input("Enter the new grade: ")

        update_student_grade(student_id, new_marks, new_grade)
    except ValueError:
        print("Invalid input. Please enter numeric values for ID and marks.")
#########################################################################################################
if __name__ == '__main__':
    get_grade8_table()
    populate_students()
