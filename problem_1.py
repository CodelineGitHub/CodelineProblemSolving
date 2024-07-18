import re


# vilidation of user name 
def validate_username(username):
    if not username:
        return "Username should not be empty."
    if len(username) > 50:
        return "Username should not exceed 50 characters."
    return None
# vilidation of Password
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
# vilidation of Email
def validate_email(email):
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if not re.match(email_pattern, email):
        return "Invalid email address."
    return None
#main 
def main():
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    email = input("Enter Email: ")

    username_error = validate_username(username)
    if username_error:
        print(f"Username Error: {username_error}")

    password_error = validate_password(password)
    if password_error:
        print(f"Password Error: {password_error}")

    email_error = validate_email(email)
    if email_error:
        print(f"Email Error: {email_error}")

    if not (username_error or password_error or email_error):
        print("All inputs are valid!")

if __name__ == "__main__":
    main()
