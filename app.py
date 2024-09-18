import argparse
import subprocess

def app():
    parser = argparse.ArgumentParser(description="School Management CLI")
    parser.add_argument('role', choices=['principal', 'teacher'], help="Role to login as")
    parser.add_argument('--view', action='store_true', help="View teachers (for teachers only)")

    args = parser.parse_args()

    if args.role == 'main':
        subprocess.run(['python', 'main.py'])
    elif args.role == 'principal':
        if args.view:
            subprocess.run(['python', 'principal.py'])
        else:
            print("For teachers, use --view to view teachers.")
    elif args.role == 'teachers':
        if args.view:
            subprocess.run(['python','teachers.py'])
        else:
            print("For students, use --view to view students.")
    
if __name__ == "__app__":
    app()
