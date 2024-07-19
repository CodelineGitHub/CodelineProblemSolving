import re
def validate_username(username):
    if not username:
        return "Username cannot be empty."
    if len(username) > 50:
        return "Username cannot exceed 50 characters."
    return None

def validate_password(password):
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Password must contain at least one special symbol."
    if not re.search(r"\d", password):
        return "Password must contain at least one number."
    if not re.search(r"[A-Z]", password):
        return "Password must contain at least one uppercase letter."
    if not re.search(r"[a-z]", password):
        return "Password must contain at least one lowercase letter."
    return None

def validate_email(email):
    if "@" not in email:
        return "Email must contain @ symbol."
    local, _, domain = email.partition("@")
    if not local.isalnum():
        return "Email must have alphanumeric characters before @."
    if "." not in domain or not domain.replace(".", "").isalpha():
        return "Email domain must have letters and . character."
    return None

def main():
    print("User Login Validation")
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    email = input("Enter Email: ")

    username_invalid = validate_username(username)
    password_invalid = validate_password(password)
    email_invalid = validate_email(email)

    if username_invalid:
        print(f"Username invalid: {username_invalid}")
    if password_invalid:
        print(f"Password invalid: {password_invalid}")
    if email_invalid:
        print(f"Email invalid: {email_invalid}")

    if not username_invalid and not password_invalid and not email_invalid:
        print("All inputs are valid!")

if __name__ == "__main__":
    main()
