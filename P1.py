import re

def validate_username(username):
    if not username:
        return "Username is invalid. (Empty)"
    elif len(username) > 50:
        return "Username is invalid. (Too long)"
    else:
        return "Username is valid."

def validate_password(password):
    if len(password) < 8:
        return "Password is invalid. (Too short)"
    if not re.search(r"[A-Z]", password):
        return "Password is invalid. (No uppercase letter)"
    if not re.search(r"[a-z]", password):
        return "Password is invalid. (No lowercase letter)"
    if not re.search(r"\d", password):
        return "Password is invalid. (No number)"
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Password is invalid. (No special character)"
    return "Password is valid."

def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pattern, email):
        return "Email is valid."
    else:
        return "Email is invalid."

def main():
    print("Enter the following details:")

    username = input("Username: ")
    password = input("Password: ")
    email = input("Email: ")

    print("\nValidation Results:")
    print(validate_username(username))
    print(validate_password(password))
    print(validate_email(email))

if __name__ == "__main__":
    main()