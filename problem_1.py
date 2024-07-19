import re

def validate_username(username):
    if not username:
        return "Username should not be empty."
    if len(username) > 50:
        return "Username should not exceed more than 50 characters."
    return "Valid username."

def validate_password(password):
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Password must contain at least one special symbol."
    if not re.search(r'\d', password):
        return "Password must contain at least one number."
    if not re.search(r'[A-Z]', password) or not re.search(r'[a-z]', password):
        return "Password must contain both uppercase and lowercase characters."
    return "Valid password."

def validate_email(email):
    if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
        return "Invalid email address."
    return "Valid email address."

def main():
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    email = input("Enter Email: ")

    print(f"Username validation: {validate_username(username)}")
    print(f"Password validation: {validate_password(password)}")
    print(f"Email validation: {validate_email(email)}")

if __name__ == "__main__":
    main()
