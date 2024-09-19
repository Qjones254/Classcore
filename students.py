import sqlite3

def create_combined_table():
    CONN = sqlite3.connect('school.db')
    cursor = CONN.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            grade_level TEXT,
            first_name TEXT,
            last_name TEXT,
            teacher TEXT,
            marks REAL,
            grade TEXT       
        )
    ''')
    CONN.commit()
    print("Combined students tables successfully")
    CONN.close()

def populate_combined_table():
    CONN = sqlite3.connect('school.db')
    cursor = CONN.cursor()
    #Clear existing data in the combined table
    cursor.execute('DELETE FROM students')
    #Combine data from all grades
    query='''
       INSERT INTO students ( grade_level,first_name, last_name, teacher, marks, grade)
    SELECT 'Grade 1', first_name, last_name, teacher, marks, grade FROM grade1
    UNION ALL
    SELECT 'Grade 2', first_name, last_name, teacher, marks, grade FROM grade2
    UNION ALL
    SELECT 'Grade 3', first_name, last_name, teacher, marks, grade FROM grade3
    UNION ALL
    SELECT 'Grade4',first_name, last_name, teacher, marks, grade FROM grade4
     UNION ALL
    SELECT 'Grade5',first_name, last_name, teacher, marks, grade FROM grade5
     UNION ALL
    SELECT 'Grade6',first_name, last_name, teacher, marks, grade FROM grade6
     UNION ALL
    SELECT 'Grade7',first_name, last_name, teacher, marks, grade FROM grade7
     UNION ALL
    SELECT 'Grade8',first_name, last_name, teacher, marks, grade FROM grade8

'''
    cursor.execute(query)
    CONN.commit()
    print("Combined students table populaed successfully")
    CONN.close()

def get_all_students():
    CONN=sqlite3.connect('school.db')
    cursor=CONN.cursor()

    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()

    for student in students:
        print(student)

    CONN.close()

if __name__ == '__main__':
    create_combined_table()
    populate_combined_table()
    get_all_students()