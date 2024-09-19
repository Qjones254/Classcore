import sqlite3
from tabulate import tabulate
from rich.console import Console

console=Console()

def students_menu():
    while True:
       console.print("1) View Exams",style='purple')
       console.print("2) Exit",style='red')
       choice = int(input("Enter your Choice: "))
       if choice == 1:
           view_exams()
       else:
           break
    
def create_exams_table():
        CONN = sqlite3.connect('school.db')
        cursor = CONN.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS exams(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                term TEXT NOT NULL,
                grade_taking TEXT NOT NULL,
                beginning DATE NOT NULL,
                ending DATE NOT NULL      
            )
        ''')
        CONN.commit()
        console.print("Created exams table successfully",style='red')
        CONN.close()
###############################################################################################################
def insert_exam(name, term, grade_taking, beginning, ending):
    # Connecting to the database
    CONN = sqlite3.connect('school.db')  
    cursor = CONN.cursor()  
    # Insert a new exam
    cursor.execute('''
       INSERT INTO exams(name, term, grade_taking, beginning, ending)
       VALUES(?,?,?,?,?)
    ''', (name, term, grade_taking, beginning, ending))

    CONN.commit()
    print("Exam added successfully")
    CONN.close()
##############################################################################################################
def populate_exams():
    # Connecting to the database
    CONN = sqlite3.connect('school.db')  
    cursor = CONN.cursor()
    
    # Check if the table is empty
    cursor.execute('SELECT COUNT(*) FROM exams')
    count = cursor.fetchone()[0]

    if count == 0:
        # Insert students only if the table is empty
        exams = [
            ('Jeska', 'Term1', 'All', '2022-01-16', '2022-01-19'),
            ('Mid-Term', 'Term1', 'All', '2022-02-20', '2022-02-22'),
            ('End-Term', 'Term1', 'All', '2022-04-06', '2022-04-08'),
            ('Mid-Term', 'Term2', 'All', '2022-07-10', '2022-07-12'),
            ('End-Term', 'Term2', 'All', '2022-08-05', '2022-01-10'),
            ('End-Term', 'Term3', 'Grade1-Grade7', '2022-10-26', '2022-10-30'),
            ('K.C.S.E', 'Term3', 'Grade8', '2022-11-16', '2022-12-12')
            
        ]

        for exam in exams:
            insert_exam(*exam)
    else:
        print("Examss already exist in the database.")
    
    CONN.close()
######################################################################
def view_exams():
    CONN = sqlite3.connect('school.db')
    cursor = CONN.cursor()

    cursor.execute('SELECT * FROM exams')
    exams = cursor.fetchall()

    if not exams:
        print("No exams found!")
    else:
        headers =['ID','name','term','grade_taking','beginning','ending']
        print(tabulate(exams,headers=headers,tablefmt='pretty'))

if __name__ == '__main__':
    create_exams_table()
    populate_exams()


