import sqlite3

def get_grade2_table():
    # Connecting to the database
    CONN = sqlite3.connect('school.db')
    cursor = CONN.cursor()
    # Creating students table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS grade2(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            teacher TEXT,
            marks REAL,
            grade TEXT       
        )
    ''')
    CONN.commit()
    print("Grade2 Students table added successfully!")
    CONN.close()

def insert_student(first_name, last_name, teacher, marks, grade):
    # Connecting to the database
    CONN = sqlite3.connect('school.db')  
    cursor = CONN.cursor()  
    # Insert a new student
    cursor.execute('''
       INSERT INTO grade2(first_name, last_name, teacher, marks, grade)
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
    cursor.execute('SELECT COUNT(*) FROM grade2')
    count = cursor.fetchone()[0]

    if count == 0:
        # Insert students only if the table is empty
        students = [
            ('Maximus', 'Onesmus', 'John Magufuli', 80.2, 'B'),
            ('Goeffret', 'Ngnga', 'John Magufuli', 83.4, 'A'),
            ('Jim', 'Pele', 'John Magufuli', 54.0, 'D'),
            ('Matthew', 'Kimani', 'John Magufuli', 80.2, 'B'),
            ('Felix', 'Omanyala', 'John Magufuli', 76.2, 'B'),
            ('Erick', 'Kalama', 'John Magufuli', 33.2, 'E'),
            ('Kalistus', 'Opolo', 'John Magufuli', 60.0, 'C'),
            ('Hose', 'Musaku', 'John Magufuli', 96.7, 'A'),
            ('Caleb', 'Kipkemoi', 'John Magufuli', 55.5, 'C'),
            ('Ian', 'Ketwa', 'John Magufuli', 87.3, 'B')
        ]

        for student in students:
            insert_student(*student)
    else:
        print("Students already exist in the database.")
    
    CONN.close()

if __name__ == '__main__':
    get_grade2_table()
    populate_students()
