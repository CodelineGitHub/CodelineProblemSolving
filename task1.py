import re

def check_username(name):
    return 0 < len(name) <= 50

def check_password(pw):
    return (
        len(pw) >= 8 and
        re.search("[A-Z]", pw) and
        re.search("[a-z]", pw) and
        re.search("[0-9]", pw) and
        re.search("[!@#$%^&*]", pw)
    )

def check_email(mail):
    if "@" not in mail:
        return False
    user, dom = mail.split("@")
    return re.match(r"^[a-zA-Z0-9]+", user) and re.match(r"[a-zA-Z]+\.[a-zA-Z]+$", dom)

# Validate user login information
username = input("Username: ")
password = input("Password: ")
email = input("Email: ")

username_valid = "valid" if check_username(username) else "invalid"
password_valid = "valid" if check_password(password) else "invalid"
email_valid = "valid" if check_email(email) else "invalid"

print("Username is", username_valid)
print("Password is", password_valid)
print("Email is", email_valid)
