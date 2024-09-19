import sqlite3

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

if __name__ == '__main__':
    get_grade8_table()
    populate_students()
