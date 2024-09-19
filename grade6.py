import sqlite3

def get_grade6_table():
    # Connecting to the database
    CONN = sqlite3.connect('school.db')
    cursor = CONN.cursor()
    # Creating students table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS grade6(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            teacher TEXT,
            marks REAL,
            grade TEXT       
        )
    ''')
    CONN.commit()
    print("Grade6 Students table added successfully!")
    CONN.close()

def insert_student(first_name, last_name, teacher, marks, grade):
    # Connecting to the database
    CONN = sqlite3.connect('school.db')  
    cursor = CONN.cursor()  
    # Insert a new student
    cursor.execute('''
       INSERT INTO grade6(first_name, last_name, teacher, marks, grade)
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
    cursor.execute('SELECT COUNT(*) FROM grade6')
    count = cursor.fetchone()[0]

    if count == 0:
        # Insert students only if the table is empty
        students = [
            ('Moses', 'Njiiri', 'Victor Kalili', 80.2, 'B'),
            ('Melchior', 'Balthazar', 'Victor Kalili', 5.2, 'F'),
            ('Jordan', 'Mwangi', 'Victor Kalili', 54.0, 'D'),
            ('Purity', 'Wanjiku', 'Victor Kalili', 70.2, 'C'),
            ('Freddy', 'Katana', 'Victor Kalili', 96.2, 'A'),
            ('Effie', 'Wekesa', 'Victor Kalili', 95.2, 'A'),
            ('Menje', 'Muloki', 'Victor Kalili', 60.0, 'C'),
            ('Pauline', 'Mwikali', 'Victor Kalili', 76.7, 'B'),
            ('Christine', 'Waithera', 'Victor Kalili', 98.5, 'A'),
            ('Imelda', 'George', 'Victor Kalili', 77.3, 'C')
        ]

        for student in students:
            insert_student(*student)
    else:
        print("Students already exist in the database.")
    
    CONN.close()

if __name__ == '__main__':
    get_grade6_table()
    populate_students()
