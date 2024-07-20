import re


def validate_username(username):
    return 0 < len(username) <= 50


def validate_password(password):
    if (len(password) < 8 or
            not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) or  # special char
            not re.search(r"\d", password) or  # digit
            not re.search(r"[A-Z]", password) or  # uppercase
            not re.search(r"[a-z]", password)  # lowercase
    ):
        return False
    return True


def validate_email(email):
    if not re.match(r"^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
        return False
    return True


def main():
    username = input("Username: ")
    password = input("Password: ")
    email = input("Email: ")

    # A dictionary to map True/False to text
    dicti = {
        True: "valid",
        False: "invalid"
    }

    print(f"Username is {dicti[validate_username(username)]}.")
    print(f"Password is {dicti[validate_password(password)]}.")
    print(f"Email is {dicti[validate_email(email)]}.")


if __name__ == '__main__':
    main()
