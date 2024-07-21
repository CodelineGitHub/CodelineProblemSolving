import re

def validate_username(username):
if len(username) == 0 or len(username) > 50:
return False
return True

def validate_password(password):
if len(password) < 8:
return False
if not re.search("[A-Z]", password) or not re.search("[a-z]", password):
return False
if not re.search("[0-9]", password) or not re.search("[!@#$%^&*]", password):
return False
return True

def validate_email(email):
if "@" not in email:
return False
username, domain = email.split("@")
if not re.match(r"^[a-zA-Z0-9]+", username) or not re.match(r"[a-zA-Z]+\.[a-zA-Z]+$", domain):
return False
return True

# Input user login information
username = input("Username: ")
password = input("Password: ")
email = input("Email: ")

# Validate user login information
username_valid = "valid" if validate_username(username) else "invalid"
password_valid = "valid" if validate_password(password) else "invalid"
email_valid = "valid" if validate_email(email) else "invalid"

# Output validation results
print("Username is", username_valid)
print("Password is", password_valid)
print("Email is", email_valid)
```
