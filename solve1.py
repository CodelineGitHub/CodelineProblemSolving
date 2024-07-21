import re

def is_valid_username(username):
    return 0 < len(username) <= 50

def is_valid_password(password):
    return (len(password) >= 8 and
            re.search("[A-Z]", password) and
            re.search("[a-z]", password) and
            re.search("[0-9]", password) and
            re.search("[!@#$%^&*]", password))

def is_valid_email(email):
    if "@" not in email:
        return False
    username, domain = email.split("@")
    return re.match(r"^[a-zA-Z0-9]+$", username) and re.match(r"[a-zA-Z]+\.[a-zA-Z]+$", domain)

username = input("Username: ")
password = input("Password: ")
email = input("Email: ")

print("Username is", "valid" if is_valid_username(username) else "invalid")
print("Password is", "valid" if is_valid_password(password) else "invalid")
print("Email is", "valid" if is_valid_email(email) else "invalid")
