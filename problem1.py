import re

def validate_username(username):
    if not username:
        return False, "Username is invalid."
    if len(username) > 50:
        return False, "Username is invalid."
    return True, ""

def validate_password(password):
    if len(password) < 8:
        return False, "Password is invalid."
    if not re.search("[!@#$%^&*()-_=+{};:,<.>/?]", password):
        return False, "Password is invalid."
    if not re.search("[0-9]", password):
        return False, "Password is invalid."
    if not re.search("[A-Z]", password) or not re.search("[a-z]", password):
        return False, "Password is invalid."
    return True, ""

def validate_email(email):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return False, "Email is invalid."
    return True, ""

def main():
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    email = input("Email: ").strip()

    username_valid, username_error = validate_username(username)
    password_valid, password_error = validate_password(password)
    email_valid, email_error = validate_email(email)

    if username_valid:
        if username_valid:
            print("username is valid")
    else:

        if not username_valid:
            print( username_error)
       
    if password_valid: 
        if password_valid:
            print("password is valid")
    else:
         if not password_valid:
            print( password_error)
            
    
    if email_valid: 
         if email_valid:
            print("email is valid")
    
    else:
        if not email_valid:
            print( email_error)    

if __name__ == "__main__":
    main()