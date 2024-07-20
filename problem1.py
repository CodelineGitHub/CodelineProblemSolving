import re


def validate_username(username):
    if len(username) == 0:
        return "Username is invalid."
    if len(username) > 50:
        return "Username is invalid."
    return "Username is valid."


def validate_password(password):
    if len(password) < 8:
        return "Password is invalid."
    if not re.search("[a-zA-Z]", password):
        return "Password is invalid."
    if not re.search("[0-9]", password):
        return "Password is invalid."
    if not re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        return "Password is invalid."
    if not re.search("[A-Z]", password) or not re.search("[a-z]", password):
        return "Password is invalid."
    return "Password is valid."


def validate_email(email):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return "Email is invalid."
    return "Email is valid."


def main():
    username = input("Username: ")
    password = input("Password: ")
    email = input("Email: ")

    username_result = validate_username(username)
    password_result = validate_password(password)
    email_result = validate_email(email)

    print(username_result)
    print(password_result)
    print(email_result)


if __name__ == "__main__":
    main()