

def login():
    username = input("Username: ")
    password = input("Password: ")

    try:
        with open("data/users.txt", "r") as file:
            for line in file:
                user, pw, role = line.strip().split("|")

                if username == user and password == pw:
                    print(f"\nWelcome {user}!")
                    return user, role

    except FileNotFoundError:
        print("User file not found!")

    print("\nInvalid username or password!")
    return None, None