import re

def validate_username(username):
    if not username:
        return "Username should not be empty."
    if len(username) > 50:
        return "Username should not exceed 50 characters."
    return "Username is valid."

def validate_password(password):
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Password must contain at least one special symbol."
    if not re.search(r'[0-9]', password):
        return "Password must contain one or more numbers."
    if not re.search(r'[A-Z]', password):
        return "Password must contain one or more uppercase characters."
    if not re.search(r'[a-z]', password):
        return "Password must contain one or more lowercase characters."
    return "Password is valid."

def validate_email(email):
    if "@" not in email:
        return "Email should contain the '@' symbol."
    local_part, domain = email.split("@", 1)
    if not local_part.isalnum():
        return "Email should have alphanumeric characters before the '@' symbol."
    if not re.match(r'^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', domain):
        return "Email should have letters and '.' character in the domain part."
    return "Email is valid."

def main():
    username = input("Username: ")
    password = input("Password: ")
    email = input("Email: ")

    print(validate_username(username))
    print(validate_password(password))
    print(validate_email(email))

if __name__ == "__main__":
    main()