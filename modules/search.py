def search_menu():
    while True:
        print("\n===== SEARCH MENU =====")
        print("[1] Search Room")
        print("[2] Search Guest")
        print("[3] Search Reservation")
        print("[4] Back")

        choice = input("\nSelect option: ")

        if choice == "1":
            keyword = input("Enter Room ID: ")

            try:
                found = False

                with open("data/rooms.txt", "r") as file:
                    for line in file:
                        if keyword in line:
                            print("\nFound:")
                            print(line)
                            found = True

                if not found:
                    print("Room not found!")

            except FileNotFoundError:
                print("No room records found!")

        elif choice == "2":
            keyword = input("Enter Guest ID: ")

            try:
                found = False

                with open("data/guests.txt", "r") as file:
                    for line in file:
                        if keyword in line:
                            print("\nFound:")
                            print(line)
                            found = True

                if not found:
                    print("Guest not found!")

            except FileNotFoundError:
                print("No guest records found!")

        elif choice == "3":
            keyword = input("Enter Reservation ID: ")

            try:
                found = False

                with open("data/reservations.txt", "r") as file:
                    for line in file:
                        if keyword in line:
                            print("\nFound:")
                            print(line)
                            found = True

                if not found:
                    print("Reservation not found!")

            except FileNotFoundError:
                print("No reservation records found!")

        elif choice == "4":
            break

        else:
            print("Invalid option!")