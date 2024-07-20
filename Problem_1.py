import re

def validate_username(username):
    if len(username) == 0:
        return False, "Username must not be empty."
    if len(username) > 50:
        return False, "Username must not exceed 50 characters."
    return True, ""

def validate_password(password):
    # Password must consist of at least 8 characters
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    
    # Password must contain at least one special symbol
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False, "Password must contain at least one special symbol (!@#$%^&*(),.?\":{}|<>)."
    
    # Password must have one or more numbers
    if not any(char.isdigit() for char in password):
        return False, "Password must contain at least one digit."
    
    # Password must contain one or more uppercase and lowercase letters
    if not any(char.isupper() for char in password) or not any(char.islower() for char in password):
        return False, "Password must contain both uppercase and lowercase letters."
    
    return True, ""

def validate_email(email):
    if '@' not in email:
        return False, "Email must contain the '@' symbol."
    
    # Split email into local part and domain part
    local_part, domain_part = email.rsplit('@', 1)
    
    # Validate local part
    if not local_part.isalnum():
        return False, "Email local part must contain only alphanumeric characters."
    
    # Validate domain part
    if not re.match(r'^[a-zA-Z0-9][a-zA-Z0-9.-]+[a-zA-Z0-9]$', domain_part):
        return False, "Invalid email domain format."
    
    return True, ""

def main():
    print("Welcome to User Login Validation Program!\n")
    
    username = input("Enter username: ")
    password = input("Enter password: ")
    email = input("Enter email address: ")
    
    # Validate username
    is_valid_username, username_error = validate_username(username)
    if not is_valid_username:
        print(f"Username validation failed: {username_error}")
        return
    
    # Validate password
    is_valid_password, password_error = validate_password(password)
    if not is_valid_password:
        print(f"Password validation failed: {password_error}")
        return
    
    # Validate email
    is_valid_email, email_error = validate_email(email)
    if not is_valid_email:
        print(f"Email validation failed: {email_error}")
        return
    
    print("\nCongratulations! All inputs are valid.")

if __name__ == "__main__":
    main()

