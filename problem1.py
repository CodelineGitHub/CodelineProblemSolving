import re

def is_valid_username(username):
    if not username:
        return False, "Username should not be empty."
    if len(username) > 50:
        return False, "Username should not exceed 50 characters."
    return True, "Valid username."

def is_valid_password(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Password must contain at least one special symbol."
    if not re.search(r"\d", password):
        return False, "Password must contain at least one number."
    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter."
    if not re.search(r"[a-z]", password):
        return False, "Password must contain at least one lowercase letter."
    return True, "Valid password."

def is_valid_email(email):
    if "@" not in email:
        return False, "Email should contain '@' symbol."
    parts = email.split("@")
    if len(parts) != 2:
        return False, "Email should have one '@' symbol."
    if not re.match(r"^[a-zA-Z0-9_.+-]+$", parts[0]):
        return False, "Invalid characters before '@' symbol."
    domain_parts = parts[1].split(".")
    if len(domain_parts) < 2:
        return False, "Email domain should contain a '.' character."
    for part in domain_parts:
        if not re.match(r"^[a-zA-Z]+$", part):
            return False, "Email domain should contain only letters after '.'"
    return True, "Valid email."

def main():
    username = input("Enter Username: ")
    valid, message = is_valid_username(username)
    print(message)
    if not valid:
        return

    password = input("Enter Password: ")
    valid, message = is_valid_password(password)
    print(message)
    if not valid:
        return

    email = input("Enter Email: ")
    valid, message = is_valid_email(email)
    print(message)
    if not valid:
        return

    print("All inputs are valid!")

if __name__ == "__main__":
    main()
