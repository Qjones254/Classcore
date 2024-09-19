import sqlite3
from tabulate import tabulate
from rich import print
from grade1 import view_grade_students,change_student_grades
from grade2 import view_grade_students,change_student_grades
from grade3 import view_grade_students,change_student_grades
from grade4 import view_grade_students,change_student_grades
from grade5 import view_grade_students,change_student_grades
from grade6 import view_grade_students,change_student_grades
from grade7 import view_grade_students,change_student_grades

def authenticate_teacher():
    name = input("Enter your name >>> ")
    print(f"Welcome {name}")
    password = input("Enter password: ")
    if password != "Admin":
        print("Enter a valid password!")
        return None
    return name
def view_students():
    CONN = sqlite3.connect('school.db')
    cursor = CONN.cursor()

    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()

    if not students:
        print("No students found!")
    else:
        headers =['ID','first_name','last_name','teacher','marks','grade']
        print(tabulate(students,headers=headers,tablefmt='pretty'))

def teacher_menu():
    name = authenticate_teacher()
    if name:
        while True:
            print("1) View classes")
            print("2) View students")
            print("3) Exit")
            choice = int(input())
        
            if choice == 1:
                mark_grades()
            elif choice == 2:
                view_students()
            elif choice == 3:
                break
            else:
                print("Invalid choice. Try again.")
            
def mark_grades():
    while True:
        print("What grade do you teach?")
        print("1) Grade 1")
        print("2) Grade 2")
        print("3) Grade 3")
        print("4) Grade 4")
        print("5) Grade 5")
        print("6) Exit.")
        choice = int(input())
        if choice == 6:
            break
        elif  1<=choice<=5:
         classes_option()
        else:
         print("Invalid choice. Try again.")

def classes_option():
  while True:
    print("1) View grade students")
    print("2) Change student grades")
    print("3) Exit")
    choice = int(input())
    if choice == 1:
        view_grade_students()
    elif choice == 2:
        change_student_grades()
    elif choice == 3:
          break
    


