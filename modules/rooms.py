def room_menu():
    while True:
        print("\n===== ROOM MANAGEMENT =====")
        print("[1] Add Room")
        print("[2] View Rooms")
        print("[3] Back")

        choice = input("\nSelect option: ")

        if choice == "1":
            room_id = input("Room ID: ")
            room_type = input("Room Type: ")
            price = input("Price: ")

            with open("data/rooms.txt", "a") as file:
                file.write(f"{room_id}|{room_type}|Available|{price}\n")

            print("\nRoom added successfully!")

        elif choice == "2":
            try:
                with open("data/rooms.txt", "r") as file:
                    print("\n===== ROOMS =====")
                    print(file.read())
            except FileNotFoundError:
                print("\nNo rooms found!")

        elif choice == "3":
            break

        else:
            print("\nInvalid option!")