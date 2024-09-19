import sqlite3

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

if __name__ == '__main__':
    get_grade7_table()
    populate_students()
