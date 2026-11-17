import os
from colorama import Fore
from modules.rooms import room_menu
from modules.guests import guest_menu
from modules.reservations import reservation_menu
from modules.reports import report_menu
from modules.search import search_menu

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
        print("[5] Search")
        print("[6] Settings")
        print("[7] Logout")

        choice = input("\nSelect option: ")

        if choice == "1":
            room_menu()

        elif choice == "2":
            guest_menu()

        elif choice == "3":
            reservation_menu()

        elif choice == "4":
            report_menu()

        elif choice == "5":
            search_menu()

        elif choice == "7":
            break

        else:
            input("\nFeature coming soon. Press Enter...")