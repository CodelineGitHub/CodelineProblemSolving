
# solution problem one
import re

def validate_username(username):
    if not username:
        return False, "Username should not be empty."
    if len(username) > 50:
        return False, "Username should not exceed 50 characters."
    return True, ""

def validate_password(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    if not re.search(r"[!@#$%^&*()\-_=+{};:,<.>]", password):
        return False, "Password should contain at least one special character."
    if not re.search(r"\d", password):
        return False, "Password should contain at least one digit."
    if not re.search(r"[a-z]", password):
        return False, "Password should contain at least one lowercase letter."
    if not re.search(r"[A-Z]", password):
        return False, "Password should contain at least one uppercase letter."
    return True, ""

def validate_email(email):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return False, "Invalid email address format."
    return True, ""

def main():
    print("User Registration Form Validation")
    print("---------------------------------")

    username = input("Enter username: ")
    password = input("Enter password: ")
    email = input("Enter email address: ")

    username_valid, username_error = validate_username(username)
    if not username_valid:
        print(f"Username is invalid: {username_error}")

    password_valid, password_error = validate_password(password)
    if not password_valid:
        print(f"Password is invalid: {password_error}")

    email_valid, email_error = validate_email(email)
    if not email_valid:
        print(f"Email address is invalid: {email_error}")

    if username_valid and password_valid and email_valid:
        print("Registration Successful!")

if __name__ == "__main__":
    main()




