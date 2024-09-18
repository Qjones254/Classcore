import sqlite3

def create_database():
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()

    #Creating teachers table
    cursor.execute('''
        CREATE TABLE IS NOT EXISTS teachers(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            grade_teaching TEXT,
            pay_per_month REAL     
)
''')
    conn.commit()
    conn.close()
    print("Database and tables created successfully.")

    if __name__=="__main__":
        create_database()