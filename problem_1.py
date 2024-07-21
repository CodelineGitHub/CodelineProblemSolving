import re

def name_validation(username):
    if len(username) == 0:
        print("Username is invalid.") 
    elif len(username) > 50:
        print("Username is invalid.") 
    else:
        print("Username is valid.") 

def pass_validation(password):
    special_characters = "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?`~"
    if (len(password) >= 8 and
        any(char in special_characters for char in password) and
        any(char.isdigit() for char in password) and
        any(char.isupper() for char in password) and
        any(char.islower() for char in password)):
        print("Password is valid.")
    else:
        print("Password is invalid.")
        
def email_validation(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        print("Email is valid.")
    else:
        print("Email is invalid.")

def main():
    username= input("Username: ")
    password= input("Password: ")
    email= input("Email: ")

    print("\nValidation Results:")
    name_validation(username)
    pass_validation(password)
    email_validation(email)

# Keep the terminal window open 
    input("\nPress Enter to exit...")


main()
