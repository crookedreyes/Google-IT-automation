def hint_username(username):
    if len(username) < 3:
        print("invalid username. Must be at least 3 charachers long")
    elif len(username) > 15:
        print("Invalid username. Must be at most 15 characters long")
    else:
        print("Valid username")

username = input("Enter username\n")
hint_username(username)