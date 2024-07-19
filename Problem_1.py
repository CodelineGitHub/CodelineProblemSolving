import re

def validate_username(username):
    if not username:
        return False, "Username must not be empty."
    if len(username) > 50:
        return False, "Username must not exceed 50 characters."
    return True, ""

def validate_password(password):
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
    return True, ""

def validate_email(email):
    if "@" not in email:
        return False, "Email must contain '@' symbol."
    local, _, domain = email.partition("@")
    if not local.isalnum() or not domain.isalnum():
        return False, "Email must contain alphanumeric characters before and after '@' symbol."
    if "." not in domain:
        return False, "Email must contain characters following the domain part."
    return True, ""

def main():
    username = input("Enter username: ")
    password = input("Enter password: ")
    email = input("Enter email: ")

    is_valid, message = validate_username(username)
    if not is_valid:
        print(message)
        return

    is_valid, message = validate_password(password)
    if not is_valid:
        print(message)
        return

    is_valid, message = validate_email(email)
    if not is_valid:
        print(message)
        return

    print("All inputs are valid!")

if __name__ == "__main__":
    main()
