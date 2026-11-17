def report_menu():
    while True:
        print("\n===== REPORTS =====")
        print("[1] Room Report")
        print("[2] Guest Report")
        print("[3] Reservation Report")
        print("[4] Back")

        choice = input("\nSelect option: ")

        if choice == "1":
            try:
                with open("data/rooms.txt", "r") as file:
                    rooms = file.readlines()

                print(f"\nTotal Rooms: {len(rooms)}")

            except FileNotFoundError:
                print("\nNo room records found!")

        elif choice == "2":
            try:
                with open("data/guests.txt", "r") as file:
                    guests = file.readlines()

                print(f"\nTotal Guests: {len(guests)}")

            except FileNotFoundError:
                print("\nNo guest records found!")

        elif choice == "3":
            try:
                with open("data/reservations.txt", "r") as file:
                    reservations = file.readlines()

                print(f"\nTotal Reservations: {len(reservations)}")

            except FileNotFoundError:
                print("\nNo reservation records found!")

        elif choice == "4":
            break

        else:
            print("\nInvalid option!")