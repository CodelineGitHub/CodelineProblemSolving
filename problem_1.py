
import re

def validation():
    print("Please enter your information:")
    print("1. Enter Username")
    print("2. Enter Password")
    print("3. Enter Email")
    print("4. Exit")
    print()

def enter_username():
    while True:
        username = input("Enter your username (max 50 characters): ")
        if username.strip() == "":
            print("Username is invalid.")
        elif len(username) > 50:
            print("Username is invalid.")
        else:
            print("Username entered:", username)
            print()
            break

def enter_password():
    while True:
        password = input("Enter your password: ")
        
        # Validate password criteria
        if len(password) < 8:
            print("Password is invalid.")
        elif not re.search("[!@#$%^&*()-_=+{};:,<.>/?]", password):
            print("Password is invalid.")
        elif not re.search("[0-9]", password):
            print("Password is invalid.")
        elif not re.search("[A-Z]", password):
            print("Password is invalid.")
        elif not re.search("[a-z]", password):
            print("Password is invalid.")
        else:
            print("Password is valid.:", password)
            print()
            break

def enter_email():
    while True:
        email = input("Enter your email: ")
        
        # Validate email 
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            print("Email is invalid.")
        else:
            print("Email is valid:", email)
            print()
            break

#loop
while True:
    validation()
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        enter_username()
    elif choice == '2':
        enter_password()
    elif choice == '3':
        enter_email()
    elif choice == '4':
        print("Exiting program")
        break
    else:
        print("Invalid choice. Enter a number from 1 to 4.")
