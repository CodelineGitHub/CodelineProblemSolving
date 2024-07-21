
def is_valid_username(username):

if len(username) == 0:

print("Username cannot be empty.")
return False
if len(username) > 50:
print("Username should not exceed 50 characters.")

return False
return True


def is_valid_password(password):

if len(password) < 8:
print("Password must be at least 8 characters long.")
return False

if not any(char in "!@#$%^&*()" for char in password):
print("Password must contain at least one special symbol.")
return False

if not any(char.isdigit() for char in password):

print("Password must contain at least one number.")
return False

if not any(char.isupper() for char in password):
print("Password must contain at least one uppercase character.")

return False

if not any(char.islower() for char in password):
print("Password must contain at least one lowercase character.")
return False

return True


def is_valid_email(email):

if "@" not in email:
print("Email must contain '@' symbol.")
return False

before_at, after_at = email.split("@", 1)
if not before_at.isalnum():
print("Email should have alphanumeric characters before '@'.")

return False

if "." not in after_at:
print("Email must contain '.' after '@'.")
return False

if not after_at.replace(".", "").isalpha():
print("Email should have letters before and after '.'.")
return False

return True


def main():

print("Please enter the following details:")

while True:

username = input("Username: ")

if is_valid_username(username):

break

while True:

password = input("Password: ")

if is_valid_password(password):
break

while True:
email = input("Email: ")

if is_valid_email(email):

break

print("All inputs are valid.")
print(f"Username: {username}")

print(f"Password: {password}")
print(f"Email: {email}")


if __name__ == "__main__":

main()
