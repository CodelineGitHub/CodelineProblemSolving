import re

def is_valid_username(username):
    if username and len(username) <= 50:
        return True
    return False

def is_valid_password(password):
    if (len(password) >= 8 and 
        any(c.islower() for c in password) and
        any(c.isupper() for c in password) and
        any(c.isdigit() for c in password) and
        any(c in "!@#$%^&*()_+-=[]{}|;:'\",.<>?/`~" for c in password)):
        return True
    return False

def is_valid_email(email):
    email_regex = re.compile(
        r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$'
    )
    if email_regex.match(email):
        return True
    return False

def main():
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    email = input("Enter Email: ")

    if is_valid_username(username):
        print("Username is valid.")
    else:
        print("Username is invalid.")

    if is_valid_password(password):
        print("Password is valid.")
    else:
        print("Password is invalid.")

    if is_valid_email(email):
        print("Email is valid.")
    else:
        print("Email is invalid.")

if __name__ == "__main__":
    main()
