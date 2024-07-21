import re

def validate_username(username):
    if not username:
        return False, "Username is Invalid, Username cannot be empty."
    if len(username) > 50:
        return False, "Username is Invalid, Username cannot exceed 50 characters"
    return True, "Username is valid."

def validate_password(password):
     # Check length
    if len(password) < 8:
        return False, "Password is Invalid, Password must be at least 8 characters long."
    
      # Check for special symbol
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False, "Password is Invalid , Password must contain at least one special symbol."
    if not any(char.isdigit() for char in password):
        return False, "Password is Invalid, Password must contain at least one number."
    if not any(char.isupper() for char in password) or not any(char.islower() for char in password):
        return False, "Password is Invalid, Password must contain both uppercase and lowercase characters."
    return True, "Password is valid."

def validate_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, email):
        return False, "Email is Invalid, Email format it should have '@' symbol and a valid domain"
    return True, "Email is valid."

def main():
    print("Welcome! Please enter your details:")
    username = input("Username: ")
    password = input("Password: ")
    email = input("Email: ")
    
    is_valid_username, username_message = validate_username(username)
    print(username_message)
    
    
    is_valid_password, password_message = validate_password(password)
    print(password_message)
    

    is_valid_email, email_message = validate_email(email)
    print(email_message)

if __name__ == "__main__":
    main()