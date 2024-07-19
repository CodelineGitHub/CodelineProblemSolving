import re
import os

def valid_username(username):
    if not username:
        return "Username is invalid."
    if len(username) > 50:
        return "Username is invalid."
    return "Username is valid."

def valid_password(password):
    if len(password) < 8:
        return "Password is invalid."
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Password is invalid."
    if not re.search(r'[0-9]', password):
        return "Password is invalid."
    if not re.search(r'[A-Z]', password):
        return "Password is invalid."
    if not re.search(r'[a-z]', password):
        return "Password is invalid."
    return "Password is valid."

def valid_email(email):
    email_regex = re.compile(
        r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    )
    if not email_regex.match(email):
        return "Email is invalid."
    return "Email is valid."

def main():

    username = input("Username: ")
    password = input("Password: ")
    email = input("Email: ")

    username_result = valid_username(username)
    password_result = valid_password(password)
    email_result = valid_email(email)


    print("\n")
    print(username_result)
    print(password_result)
    print(email_result)

if __name__ == "__main__":
    main()
