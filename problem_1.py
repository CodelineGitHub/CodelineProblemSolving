
import re


def is_valid_username(username):
    return bool(username) and len(username) <= 50


def is_valid_password(password):
    if len(password) < 8:
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    return True


def is_valid_email(email):
    if '@' not in email:
        return False
    local, domain = email.split('@', 1)
    if not local.isalnum():
        return False
    if '.' not in domain:
        return False
    subdomains = domain.split('.')
    if len(subdomains) < 2:
        return False
    if not all(subdomain.isalpha() for subdomain in subdomains):
        return False
    return True


def main():
    username = input("Username: ")
    password = input("Password: ")
    email = input("Email: ")

    username_valid = is_valid_username(username)
    password_valid = is_valid_password(password)
    email_valid = is_valid_email(email)

    if username_valid:
        print("username is valid")
    else:
        print("username is invalid")

    if password_valid:
        print("password is valid")
    else:
        print("Password is invalid.")

    if email_valid:
        print("email is valid")
    else:
        print("Email is invalid.")

    if username_valid and password_valid and email_valid:
        print("All inputs are valid!")


if __name__ == "__main__":
    main()
