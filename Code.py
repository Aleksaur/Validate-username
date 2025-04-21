special_characters = "!@#$%^&*()-+?_=,<>/"

while True:
    username = input("Enter your username: ")

    if len(username) < 6:
        print("Username must be longer than 6 characters")

    elif len(username) > 12:
        print("Username mustn't be longer than 12 characters")

    elif " " in username:
        print("Username mustn't contain spaces")

    elif username.isdigit():
        print("Username must contain a letter")

    elif username.isalpha():
        print("Username must contain a number")

    elif username.islower():
        print("Username must contain an uppercase letter")

    elif username.isupper():
        print("Username must contain a lowercase letter")

    elif not any(c in special_characters for c in username):
        print("Username must contain a special character")

    else:
        print(f"Welcome, {username}")
        break