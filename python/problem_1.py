import re

def validate_username(username):
    if not username:
        return False, "(invalid) Username cannot be empty."
    if len(username) > 50:
        return False, "(invalid) Username cannot exceed 50 characters."
    return True, "Username is valid."

def validate_password(password):
    if len(password) < 8:
        return False, "(invalid) Password must be at least 8 characters long."
    if not re.search(r"[!@#$%^&*()_+{}\[\]:;<>,.?~\\-]", password):
        return False, "(invalid) Password must contain at least one special symbol."
    if not re.search(r"\d", password):
        return False, "(invalid) Password must contain at least one digit."
    if not re.search(r"[a-z]", password) or not re.search(r"[A-Z]", password):
        return False, " (invalid) Password must contain both uppercase and lowercase letters."
    return True, "Password is valid."

def validate_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+$"
    if not re.match(pattern, email):
        return False, "Invalid email format."
    return True, "Email is valid."

def main():
    print("Welcome to User Registration Program")
    print("===================================")
    
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    email = input("Enter Email: ")
    
    username_valid, username_message = validate_username(username)
    password_valid, password_message = validate_password(password)
    email_valid, email_message = validate_email(email)
    
    print("\nValidation Results:")
    print("===================")
    print(f"Username: {username_message}")
    print(f"Password: {password_message}")
    print(f"Email: {email_message}")
    
    if username_valid and password_valid and email_valid:
        print("\nRegistration Successful!")
        print("===========================")
        print("User Details:")
        print(f"Username: {username}")
        print(f"Password: {password}")
        print(f"Email: {email}")
    else:
        print("\nRegistration Failed. Please correct the errors and try again.")

if __name__ == "__main__":
    main()
