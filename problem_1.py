import re

def validate_username(username):
    if not username or len(username) > 50:
        return "Username is invalid."
    return "Username is valid."

def validate_password(password):
    if len(password) < 8 or not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) or not re.search(r"\d", password) or not re.search(r"[A-Z]", password) or not re.search(r"[a-z]", password):
        return "Password is invalid."
    return "Password is valid."

def validate_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(email_regex, email):
        return "Email is invalid."
    return "Email is valid."

def main():
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    email = input("Enter Email: ")

    print(validate_username(username))
    print(validate_password(password))
    print(validate_email(email))

if __name__ == "__main__":
    main()

