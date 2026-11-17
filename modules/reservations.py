def reservation_menu():
    while True:
        print("\n===== RESERVATION MANAGEMENT =====")
        print("[1] Add Reservation")
        print("[2] View Reservations")
        print("[3] Back")

        choice = input("\nSelect option: ")

        if choice == "1":
            reservation_id = input("Reservation ID: ")
            guest_id = input("Guest ID: ")
            room_id = input("Room ID: ")
            checkin_date = input("Check-in Date: ")

            with open("data/reservations.txt", "a") as file:
                file.write(
                    f"{reservation_id}|{guest_id}|{room_id}|{checkin_date}|Reserved\n"
                )

            print("\nReservation added successfully!")

        elif choice == "2":
            try:
                with open("data/reservations.txt", "r") as file:
                    print("\n===== RESERVATIONS =====")
                    print(file.read())

            except FileNotFoundError:
                print("\nNo reservations found!")

        elif choice == "3":
            break

        else:
            print("\nInvalid option!")