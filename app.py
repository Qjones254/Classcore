import argparse
import subprocess
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def app():
    parser = argparse.ArgumentParser(description="School Management CLI")
    parser.add_argument('role', choices=['principal', 'teacher'], help="Role to login as")
    parser.add_argument('--view', action='store_true', help="View teachers (for teachers only)")

    args = parser.parse_args()

    if args.role == 'principal':
        if args.view:
            print(Fore.GREEN + Style.BRIGHT+"Opening teacher view for principal...")
            subprocess.run(['python', 'principal.py'])
        else:
            print(Fore.RED + "For teachers, use --view to view teachers.")
    elif args.role == 'teacher':
        if args.view:
            print(Fore.GREEN + "Opening student view for teacher...")
            subprocess.run(['python', 'teachers.py'])
        else:
            print(Fore.RED + "For students, use --view to view students.")

if __name__ == "__main__":
    app()

