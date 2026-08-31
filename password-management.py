import json
import os
import secrets
import string

FILE_NAME = "passwords.json"


def load_passwords():
    if not os.path.exists(FILE_NAME):
        return {}

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return {}


def save_passwords(passwords):
    with open(FILE_NAME, "w") as file:
        json.dump(passwords, file, indent=4)


def generate_password():
    length = int(input("Enter password length: "))

    characters = string.ascii_letters + string.digits + string.punctuation

    password = "".join(
        secrets.choice(characters)
        for _ in range(length)
    )

    print("\nGenerated Password:", password)


def main():
    print("🔐 PASSWORD MANAGER")
    print("1. Generate Password")

    choice = input("Enter your choice: ")

    if choice == "1":
        generate_password()
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
