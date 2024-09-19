import sqlite3

def get_grade5_table():
    # Connecting to the database
    CONN = sqlite3.connect('school.db')
    cursor = CONN.cursor()
    # Creating students table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS grade5(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            teacher TEXT,
            marks REAL,
            grade TEXT       
        )
    ''')
    CONN.commit()
    print("Grade5 Students table added successfully!")
    CONN.close()

def insert_student(first_name, last_name, teacher, marks, grade):
    # Connecting to the database
    CONN = sqlite3.connect('school.db')  
    cursor = CONN.cursor()  
    # Insert a new student
    cursor.execute('''
       INSERT INTO grade5(first_name, last_name, teacher, marks, grade)
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
    cursor.execute('SELECT COUNT(*) FROM grade5')
    count = cursor.fetchone()[0]

    if count == 0:
        # Insert students only if the table is empty
        students = [
            ('Johnny', 'Kimani', 'John Kavali', 70.2, 'C'),
            ('Mejja', 'Stephen', 'John Kavali', 46.4, 'D'),
            ('Brittany', 'Luanda', 'John Kavali', 94.0, 'A'),
            ('Lenny', 'Karanja', 'John Kavali', 80.2, 'B'),
            ('Flavia', 'Wanjiru', 'John Kavali', 66.2, 'C'),
            ('Elkanah', 'Omanyi', 'John Kavali', 5.2, 'E'),
            ('Pamela', 'Njoo', 'John Kavali', 70.0, 'C'),
            ('Juanita', 'Were', 'John Kavali', 76.7, 'B'),
            ('Esther', 'Mwende', 'John Kavali', 95.5, 'A'),
            ('Ivy', 'Mwikali', 'John Kavali', 77.3, 'B')
        ]

        for student in students:
            insert_student(*student)
    else:
        print("Students already exist in the database.")
    
    CONN.close()

if __name__ == '__main__':
    get_grade5_table()
    populate_students()
