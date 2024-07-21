import re

def validate_username(username):
    if not username:
        # Validate username is not empty
        return "Username is invalid."
    elif len(username) > 50:
        # Validate username length
        return "Username is invalid."
    else:
        return None

def validate_password(password):
    if len(password) < 8:
        # Validate password length
        return "Password is Invalid."
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        # Validate for special characters
        return "Password is Invalid."
    
    if not re.search(r'\d', password):
        # Validate for numbers
        return "Password is Invalid."
    
    if not re.search(r'[a-z]', password):
        # Validate for lower case letters
        return "Password is  Invalid."
    
    if not re.search(r'[A-Z]', password):
        # Validate for upper case letters
        return "Password is Invalid."
    
    return None

def validate_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, email):
        return "Email is invalid."
    return None

def main():
    # Input Username
    username = input("Enter your username: ")
    username_error = validate_username(username)
    if username_error:
        print(username_error)
    else:
        print("Username is valid.")

    # Input Password
    password = input("Enter your password: ")
    password_error = validate_password(password)
    if password_error:
        print(password_error)
    else:
        print("Password is valid.")

    # Input Email
    email = input("Enter your email: ")
    email_error = validate_email(email)
    if email_error:
        print(email_error)
    else:
        print("Email is valid.")

if __name__ == "__main__":
    main()
