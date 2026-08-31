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
    try:
        length = int(input("Enter password length: "))

        if length < 4:
            print("Password length must be at least 4.")
            return

        characters = string.ascii_letters + string.digits + string.punctuation

        password = "".join(
            secrets.choice(characters)
            for _ in range(length)
        )

        print("\nGenerated Password:", password)

    except ValueError:
        print("Please enter a valid number.")


def save_password():
    passwords = load_passwords()

    website = input("Enter website/app name: ").strip()
    username = input("Enter username/email: ").strip()
    password = input("Enter password: ").strip()

    if not website or not username or not password:
        print("All fields are required.")
        return

    passwords[website] = {
        "username": username,
        "password": password
    }

    save_passwords(passwords)

    print("Password saved successfully!")


def view_passwords():
    passwords = load_passwords()

    if not passwords:
        print("No passwords saved.")
        return

    print("\nSaved Passwords")

    for website, details in passwords.items():
        print("\nWebsite:", website)
        print("Username:", details["username"])
        print("Password:", details["password"])


def delete_password():
    passwords = load_passwords()

    website = input("Enter website/app name to delete: ").strip()

    if website in passwords:
        del passwords[website]
        save_passwords(passwords)
        print("Password deleted successfully!")
    else:
        print("Website not found.")


def search_password():
    passwords = load_passwords()

    search = input("Enter website/app name to search: ").strip().lower()

    found = False

    for website, details in passwords.items():
        if search in website.lower():
            print("\nWebsite:", website)
            print("Username:", details["username"])
            print("Password:", details["password"])
            found = True

    if not found:
        print("No matching password found.")


def edit_password():
    passwords = load_passwords()

    website = input("Enter website/app name to edit: ").strip()

    if website not in passwords:
        print("Website not found.")
        return

    username = input("Enter new username/email: ").strip()
    password = input("Enter new password: ").strip()

    if username:
        passwords[website]["username"] = username

    if password:
        passwords[website]["password"] = password

    save_passwords(passwords)

    print("Password updated successfully!")


def check_password_strength():
    password = input("Enter password to check: ")

    score = 0

    if len(password) >= 8:
        score += 1

    if any(char.isupper() for char in password):
        score += 1

    if any(char.islower() for char in password):
        score += 1

    if any(char.isdigit() for char in password):
        score += 1

    if any(char in string.punctuation for char in password):
        score += 1

    if score <= 2:
        print("Weak Password")
    elif score <= 4:
        print("Medium Password")
    else:
        print("Strong Password")


def main():
    while True:
        print("\n" + "=" * 35)
        print("PASSWORD MANAGER")
        print("=" * 35)

        print("1. Generate Password")
        print("2. Save Password")
        print("3. View Passwords")
        print("4. Delete Password")
        print("5. Search Password")
        print("6. Edit Password")
        print("7. Check Password Strength")
        print("8. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            generate_password()

        elif choice == "2":
            save_password()

        elif choice == "3":
            view_passwords()

        elif choice == "4":
            delete_password()

        elif choice == "5":
            search_password()

        elif choice == "6":
            edit_password()

        elif choice == "7":
            check_password_strength()

        elif choice == "8":
            print("Thank you for using Password Manager!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
