"""
Automate The Process Of Using Git Commands Such As clone, commit, branch, pull, merge, blame and stash
"""

import subprocess
from pyfiglet import figlet_format
from termcolor import cprint


logo = 'Git-Commands'


class color:
    NOTICE = '\033[91m'
    END = '\033[0m'


info = color.NOTICE + '''
Automate The Process Of Using Git Commands Such As clone, commit, branch, pull, merge, blame and stash.\n''' + color.END


def run(*args):
    return subprocess.check_call(['git'] + list(args))


def clone():
    print("\nYou Will Be Asked For The User First And Then The repository Name That You Want To clone.\n")

    user = input("User: ")
    __user__ = f'{user}'
    repo = input("Repository: ")
    __repo__ = f'{repo}'

    print("\nChoose The Local Path For Your clone.")
    local = input("Local Path: ")
    local_path = f'{local}'

    subprocess.Popen(['git', 'clone', "https://github.com/" + __user__ + "/" + __repo__ + ".git", local_path])


def commit():
    message = input("\nType In Your commit Message: ")
    commit_message = f'{message}'

    run("commit", "-am", commit_message)
    run("push", "-u", "origin", "master")


def branch():
    branch = input("\nType In The Name Of The branch You Want To Make: ")
    br = f'{branch}'

    run("checkout", "-b", br)

    choice = input("\nDo You Want To push The branch Right Now To GitHub? (y/n): ")
    choice = choice.lower()

    if choice == "y":
        run("push", "-u", "origin", br)

    elif choice == "n":
        print("\nOkay, See You Later !\n")

    else:
        print("\nInvalid Command! Use y OR n.\n")


def pull():
    print("\nPulls Changes From The Current Folder If *.git Is Initialized.")

    choice = input("\nDo You Want To Pull The Changes From GitHub? (y/n): ")
    choice = choice.lower()

    if choice == "y":
        run("pull")

    elif choice == "n":
        print("\nOkay, See You Later !\n")

    else:
        print("\nInvalid Command! Use y OR n.\n")


def fetch():
    print("\nFetches Changes From The Current Folder.")
    run("fetch")


def merge():
    branch = input("\nType In The Name Of Your Branch: ")
    br = f'{branch}'

    run("merge", br)


def reset():
    filename = input("\nType In The Name Of Your File: ")
    fl = f'{filename}'

    run("reset", fl)


def blame():
    file = input("\nType In The Name Of The File: ")
    fi = f'{file}'

    run("blame", fi)


def stash():
    print("\nDo You Want To save, list, pop, show, branch, clear or drop? ")

    cmd = 'save, li, pop, show, branch, clear and drop'

    print("\nCommands To Use: " + cmd)

    choice = input("\nType In The Command You Want To Use: ")
    choice = choice.lower()

    if choice == "save":
        message = input("\nType In Your stash Message: ")
        stash_message = f'{message}'

        run("stash", "save", stash_message)

    elif choice == "li":
        run("stash", "li")

    elif choice == "pop":
        run("stash", "pop")

    elif choice == "show":
        run("stash", "show", "-p")

    elif choice == "branch":
        branch = input("\nType In The Name Of The branch You Want To stash: ")
        br = f'{branch}'

        run("stash", "branch", br)

    elif choice == "clear":
        run("stash", "clear")

    elif choice == "drop":
        run("stash", "drop")

    else:
        print("\nNot A Valid Command!")
        print("\nUse " + cmd)


def main():
    cprint(figlet_format(logo, font='slant'), 'green')
    print(info + "\n")

    choices = 'clone, commit, branch, pull, fetch, merge, reset, blame and stash'
    print("Commands to use: " + choices)

    choose_command = input("Type In The Command You Want To Use: ")
    choose_command = choose_command.lower()

    if choose_command == "clone":
        clone()

    elif choose_command == "commit":
        commit()

    elif choose_command == "branch":
        branch()

    elif choose_command == "pull":
        pull()

    elif choose_command == "fetch":
        fetch()

    elif choose_command == "merge":
        merge()

    elif choose_command == "reset":
        reset()

    elif choose_command == "blame":
        blame()

    elif choose_command == "stash":
        stash()

    else:
        print("\nNot A Valid Command!")
        print("\nUse " + choices)


if __name__ == '__main__':
    main()
