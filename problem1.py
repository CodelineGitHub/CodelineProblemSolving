import re

def validate_username(username):
    if not username:
        return False, "Username cannot be empty."
    if len(username) > 50:
        return False, "Username should not exceed 50 characters."
    return True, ""

def validate_password(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False, "Password should contain at least one special symbol."
    if not re.search(r'[0-9]', password):
        return False, "Password should contain one or more numbers."
    if not re.search(r'[a-z]', password):
        return False, "Password should contain one or more lowercase letters."
    if not re.search(r'[A-Z]', password):
        return False, "Password should contain one or more uppercase letters."
    return True, ""

def validate_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, email):
        return False, "Invalid email format."
    return True, ""

def main():
    print("Welcome to the User Login Validation Program!")

    username = input("Enter Username: ")
    password = input("Enter Password: ")
    email = input("Enter Email: ")

    # Validate Username
    is_valid, message = validate_username(username)
    if not is_valid:
        print(f"Username Error: {message}")
        return
    
    # Validate Password
    is_valid, message = validate_password(password)
    if not is_valid:
        print(f"Password Error: {message}")
        return

    # Validate Email
    is_valid, message = validate_email(email)
    if not is_valid:
        print(f"Email Error: {message}")
        return

    print("All fields are valid!")

if __name__ == "__main__":
    main()
