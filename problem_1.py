import re

username = input("Username: ")
password = input("Password: ")
email = input("Email: ")

# validate username
if not username or len(username) > 50:
    print("Username is invalid.")
else:
    print("Username is valid.")

# validate password
if len(password) < 8 or not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) or not re.search(r"\d", password) or not re.search(r"[A-Z]", password) or not re.search(r"[a-z]", password):
    print("Password is invalid.")
else:
    print("Password is valid.")

# validate email
if "@" not in email or not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
    print("Email is invalid.")
else:
    print("Email is valid.")