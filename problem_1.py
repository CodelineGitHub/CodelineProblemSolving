import re

def validate_username(username):
    return 0 < len(username) <= 50

def validate_password(password):
    if len(password) < 8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char in '!@#$%^&*()_+-=[]{}|;:,.<>/?' for char in password):
        return False
    return True

def validate_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None

def main():
    print("User Login Validation")
    
    username = input("Enter Username: ")
    if not validate_username(username):
        print("Invalid Username: Must be 1-50 characters.")
    else:
        print("Username is valid.")

    password = input("Enter Password: ")
    if not validate_password(password):
        print("Invalid Password: Must be at least 8 characters long, contain special symbols, numbers, and both uppercase and lowercase letters.")
    else:
        print("Password is valid.")
    
    email = input("Enter Email: ")
    if not validate_email(email):
        print("Invalid Email: Must follow standard email format.")
    else:
        print("Email is valid.")

if __name__ == "__main__":
    main()
