import re

def validate_username(username):
    if not username:
        return "Username is invalid."
    if len(username) > 50:
        return "Username is invalid."
    return "Username is valid."

def validate_password(password):
    if len(password) < 8:
        return "Password is invalid."
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Password is invalid."
    if not re.search(r"\d", password):
        return "Password is invalid."
    if not re.search(r"[A-Z]", password):
        return "Password is invalid."
    if not re.search(r"[a-z]", password):
        return "Password is invalid."
    return "Password is valid."

def validate_email(email):
    if "@" not in email:
        return "Email is invalid."
    local, domain = email.split('@', 1)
    if not local.isalnum():
        return "Email is invalid."
    if '.' not in domain:
        return "Email is invalid."
    domain_name, extension = domain.rsplit('.', 1)
    if not domain_name.isalpha() or not extension.isalpha():
        return "Email is invalid."
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

