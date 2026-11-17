from colorama import init, Fore
from modules.auth import login
import os

init(autoreset=True)


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def header():
    clear()
    print(Fore.CYAN + "=" * 50)
    print(Fore.YELLOW + "          BOOKNEST HOTEL SYSTEM")
    print(Fore.CYAN + "=" * 50)
    print()


def main_menu():
    while True:
        header()

        print("[1] Login")
        print("[2] Exit")
        print()

        choice = input("Select option: ")

        if choice == "1":
            user, role = login()

            if user:
                print(f"\nLogged in as {user}")
                print(f"Role: {role}")

            input("\nPress Enter to continue...")

        elif choice == "2":
            print("\nThank you for using BookNest!")
            break

        else:
            print("\nInvalid option!")
            input("\nPress Enter to continue...")


if __name__ == "__main__":
    main_menu()