import re

def validate_username(username):
    if not username:
        return False
    if len(username) > 50:
        return False
    return True

def validate_password(password):
    if len(password) < 8:
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[A-Z]', password) or not re.search(r'[a-z]', password):
        return False
    return True

def validate_email(email):
    if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
        return False
    return True

def main():
    print("Enter your details:")
    username = input("Username: ")
    password = input("Password: ")
    email = input("Email: ")

    username_valid = validate_username(username)
    password_valid = validate_password(password)
    email_valid = validate_email(email)

    print(f"Username is {'valid' if username_valid else 'invalid'}.")
    print(f"Password is {'valid' if password_valid else 'invalid'}.")
    print(f"Email is {'valid' if email_valid else 'invalid'}.")

if __name__ == "__main__":
    main()
 
