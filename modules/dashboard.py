import os
from colorama import Fore

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def dashboard(user, role):
    while True:
        clear()

        print(Fore.CYAN + "=" * 50)
        print(Fore.YELLOW + "          BOOKNEST DASHBOARD")
        print(Fore.CYAN + "=" * 50)

        print(f"\nUser : {user}")
        print(f"Role : {role}")

        print("\n[1] Room Management")
        print("[2] Guest Management")
        print("[3] Reservation Management")
        print("[4] Reports")
        print("[5] Settings")
        print("[6] Logout")

        choice = input("\nSelect option: ")

        if choice == "6":
            break
        else:
            input("\nFeature coming soon. Press Enter...")