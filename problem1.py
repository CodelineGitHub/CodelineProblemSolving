import re

def is_valid_username(username):
    if not username:
        return False, "Username should not be empty."
    if len(username) > 50:
        return False, "Username should not exceed 50 characters."
    return True, "Username is valid."

def is_valid_password(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False, "Password should contain at least one special symbol."
    if not re.search(r'[0-9]', password):
        return False, "Password should have one or more numbers."
    if not re.search(r'[A-Z]', password) or not re.search(r'[a-z]', password):
        return False, "Password should have one or more uppercase and lowercase characters."
    return True, "Password is valid."

def is_valid_email(email):
    if "@" not in email:
        return False, "Email should have '@' symbol."
    local, _, domain = email.partition('@')
    if not local.isalnum():
        return False, "Email should have alphanumeric characters before '@'."
    if not re.match(r'[a-zA-Z]+\.[a-zA-Z]+', domain):
        return False, "Email should have letters with '.' character in between after '@'."
    return True, "Email is valid."

def main():
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    email = input("Enter Email: ")

    valid_username, username_msg = is_valid_username(username)
    valid_password, password_msg = is_valid_password(password)
    valid_email, email_msg = is_valid_email(email)

    print(username_msg)
    print(password_msg)
    print(email_msg)

if __name__ == "__main__":
    main()
