def guest_menu():
    while True:
        print("\n===== GUEST MANAGEMENT =====")
        print("[1] Add Guest")
        print("[2] View Guests")
        print("[3] Back")

        choice = input("\nSelect option: ")

        if choice == "1":
            guest_id = input("Guest ID: ")
            guest_name = input("Guest Name: ")
            contact = input("Contact Number: ")

            with open("data/guests.txt", "a") as file:
                file.write(f"{guest_id}|{guest_name}|{contact}\n")

            print("\nGuest added successfully!")

        elif choice == "2":
            try:
                with open("data/guests.txt", "r") as file:
                    print("\n===== GUESTS =====")
                    print(file.read())
            except FileNotFoundError:
                print("\nNo guests found!")

        elif choice == "3":
            break

        else:
            print("\nInvalid option!")