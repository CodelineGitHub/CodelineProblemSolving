Username=input("1. Enter Username: ")
Password=input("2. Enter Password: ")
Email=input("3. Enter Email: ")
if len(Username) > 0 and len(Username) <= 50:
    print("Username is valid")
else:
    print("Username is invalid")
has_uppercase = any(char.isupper() for char in Password)
has_lowercase = any(char.islower() for char in Password)
has_number = any(char.isdigit() for char in Password)
has_special = any(not char.isalnum() for char in Password)
if (len(Password) >= 8 and
          has_uppercase and has_lowercase and
          has_number and has_special):
    print("Password is valid")
else:
    print("Password is invalid")
def is_email_valid(email):
  """Checks if the email address has a basic valid format."""
  if "@" not in email:
    return False
  parts = Email.split("@")
  return (len(parts) == 2 and
          all(char.isalpha() for char in parts[0].split(".")) and
          all(char.isalpha() for char in parts[1].split(".")))
def main():
  if is_email_valid(Email):
    print("Email is valid")
  else:
    print("Email is invalid")

if __name__ == "__main__":
  main()