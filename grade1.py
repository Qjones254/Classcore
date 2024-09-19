import sqlite3

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
            ('Max', 'Steppan', 'Quincy Mwangi', 86.4, 'A'),
            ('Jim', 'Ludacris', 'Quincy Mwangi', 94.0, 'A'),
            ('Leon', 'Kimani', 'Quincy Mwangi', 60.2, 'B'),
            ('Ferdinand', 'Omanyala', 'Quincy Mwangi', 66.2, 'C'),
            ('Erick', 'Mbuthia', 'Quincy Mwangi', 95.2, 'A'),
            ('Collins', 'Mucheru', 'Quincy Mwangi', 40.0, 'D'),
            ('Henry', 'Musaku', 'Quincy Mwangi', 76.7, 'B'),
            ('Caleb', 'Lintir', 'Quincy Mwangi', 55.5, 'C'),
            ('Ian', 'George', 'Quincy Mwangi', 87.3, 'B')
        ]

        for student in students:
            insert_student(*student)
    else:
        print("Students already exist in the database.")
    
    CONN.close()

if __name__ == '__main__':
    get_grade1_table()
    populate_students()
