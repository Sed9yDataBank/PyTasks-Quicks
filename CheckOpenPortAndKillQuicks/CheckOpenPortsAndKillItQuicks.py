#!/usr/bin/python
"""
This Script Checks Whether A Port Is Open On Localhost And Kills It If User Runs kill Command
"""
import socket, sys
import subprocess
from pyfiglet import figlet_format
from termcolor import cprint

class color:
    NOTICE = '\033[91m'
    END = '\033[0m'

def run(*args):
    return subprocess.check_call(['kill'] + list(args))
	
port = 80
url = '127.0.0.1'

if len(sys.argv) == 2:
	try:
		port = int(sys.argv[1])
	except ValueError:
		url = str(sys.argv[1])

elif len(sys.argv) == 3:
	try:
		port = int(sys.argv[2])
		url = str(sys.argv[1])
	except ValueError:
		port = int(sys.argv[1])
		url = str(sys.argv[2])
else:
	pass

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	result = sock.connect_ex((url, port))
except OverflowError:
	print "Port Range Should Be Between 0 And 65535"
	sys.exit()

if result == 0:
	print "Port ", port, " Is Open""
else:
	print "Port ", port, " Is Closed""


def kill():
    port_number = input("\nType In Port Number That You Want To Kill: ")
    localhost = f'{port_number}'

    choice = input("\nDo You Want To Stop All Process Related To Port Number", localhost,"? (y/n): ")
    choice = choice.lower()

    if choice == "y":
        run("kill", "-9", "$(lsof -t -i:", localhost)

    elif choice == "n":
        print("\nOkay, See You Later !\n")

    else:
        print("\nInvalid Command! Use y OR n.\n")

info = color.NOTICE + '''
Automate The Process Of Killing Localhost Ports And It Related Processes.\n''' + color.END

def main():
    cprint(figlet_format(logo, font='slant'), 'white')
    print(info + "\n")

    choices = 'kill'
    print("Commands To Use: " + choices)

    choose_command = input("Type In The Command You Want To Use: ")
    choose_command = choose_command.lower()

    if choose_command == "kill":
        kill()

    else:
		print("\nNot A Valid Command! You Can Only Kill Ports For Now...")
        pass


if __name__ == '__main__':
    main()