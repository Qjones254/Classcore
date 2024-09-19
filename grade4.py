import sqlite3

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

if __name__ == '__main__':
    get_grade4_table()
    populate_students()
