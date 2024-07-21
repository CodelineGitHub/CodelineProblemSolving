import re

def UserName(username):
    if not username:
        return "Username cannot be empty."
    if len(username) > 30:
        return "Username cannot exceed 30 characters!"
    return None

def Password(password):

    if len(password) < 8:
        return "Password must be at least 8 characters long."
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Password must contain at least one special symbol."
    if not re.search(r'\d', password):
        return "Password must contain at least one number."
    if not re.search(r'[a-z]', password) or not re.search(r'[A-Z]', password):
        return "Password must contain both uppercase and lowercase characters."
    return None

def Email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, email):
        return "Invalid email address."
    return None

def main():
    print("User Login Validation")

    username = input(" Username: ")
    password = input(" Password: ")
    email = input(" Email: ")

    username_error = UserName(username)
    password_error = Password(password)
    email_error = Email(email)

    if username_error:
        print(f"Username Error: {username_error}")
    else:
        print("Username is valid.")

    if password_error:
        print(f"Password Error: {password_error}")
    else:
        print("Password is valid.")

    if email_error:
        print(f"Email Error: {email_error}")
    else:
        print("Email is valid.")

if __name__ == "__main__":
    main()
