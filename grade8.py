import sqlite3

def get_grade8_table():
    #Connecting to the database
    CONN = sqlite3.connect('school.db')
    cursor = CONN.cursor()
    #Creating students table
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

def insert_student(first_name,last_name,teacher,marks,grade):
    #Connecting to database
    CONN =sqlite3.connect('school.db')  
    cursor = CONN.cursor()  
    #Insert a new student
    cursor.execute('''
       INSERT INTO grade8(first_name,last_name,teacher,marks,grade)
       VALUES(?,?,?,?,?)
    ''',(first_name,last_name,teacher,marks,grade))

    CONN.commit()
    print(f"Student {first_name} {last_name} added successfully")
    CONN.close()

if __name__ == '__main__':
    get_grade8_table()