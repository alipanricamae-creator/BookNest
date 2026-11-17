def settings_menu():
    while True:
        print("\n===== SETTINGS =====")
        print("[1] Change Theme")
        print("[2] Change Password")
        print("[3] Back")

        choice = input("\nSelect option: ")

        if choice == "1":
            print("\nTheme feature coming soon...")

        elif choice == "2":
            print("\nPassword feature coming soon...")

        elif choice == "3":
            break

        else:
            print("\nInvalid option!")