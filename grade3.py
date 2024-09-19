import sqlite3

def get_grade3_table():
    # Connecting to the database
    CONN = sqlite3.connect('school.db')
    cursor = CONN.cursor()
    # Creating students table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS grade3(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            teacher TEXT,
            marks REAL,
            grade TEXT       
        )
    ''')
    CONN.commit()
    print("Grade3 Students table added successfully!")
    CONN.close()

def insert_student(first_name, last_name, teacher, marks, grade):
    # Connecting to the database
    CONN = sqlite3.connect('school.db')  
    cursor = CONN.cursor()  
    # Insert a new student
    cursor.execute('''
       INSERT INTO grade3(first_name, last_name, teacher, marks, grade)
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
    cursor.execute('SELECT COUNT(*) FROM grade3')
    count = cursor.fetchone()[0]

    if count == 0:
        # Insert students only if the table is empty
        students = [
            ('POlly', 'Mwangi', 'William Musyoki', 60.2, 'C'),
            ('Emanuella', 'Wanjiku', 'William Musyoki', 86.4, 'A'),
            ('Jane', 'Chepkoech', 'William Musyoki', 94.0, 'A'),
            ('Lilly', 'Mei', 'William Musyoki', 70.2, 'B'),
            ('Ferdinand', 'Omulu', 'William Musyoki', 66.2, 'C'),
            ('Johnston', 'Mbuthia', 'William Musyoki', 75.2, 'B'),
            ('Carol', 'Katrue', 'William Musyoki', 40.0, 'D'),
            ('Henry', 'Desagu', 'William Musyoki', 36.7, 'E'),
            ('Joseph', 'Kafuchi', 'William Musyoki', 0, 'F'),
            ('Lion', 'Mbiri', 'William Musyoki', 87.3, 'B')
        ]

        for student in students:
            insert_student(*student)
    else:
        print("Students already exist in the database.")
    
    CONN.close()

if __name__ == '__main__':
    get_grade3_table()
    populate_students()
