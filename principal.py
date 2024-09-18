import sqlite3

def create_database():
    CONN = sqlite3.connect('school.db')
    cursor = CONN.cursor()

#creating teachers table
    cursor.execute =('''
      CREATE TABLE IF NOT EXISTS teachers(
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          first_name TEXT,
          last_name TEXT,
          grade_teaching TEXT,
          pay_per_month REAL            
)
''')
    CONN.commit()
    CONN.close()
    print("Database and tables successfully created.")