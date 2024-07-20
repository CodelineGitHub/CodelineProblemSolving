# Input for username (Prompts the user to enter a username and stores 
#the input in the variable username.)
username = input("Enter username: ")
 
# Validate username (Checks if the username is empty. If it is, prints an error message.
#Checks if the username length exceeds 50 characters. If it does, prints an error message.
# If the username passes both checks, proceeds to the next block of code.)
if not username:
    print("Error: Username cannot be empty.")
elif len(username) > 50:
    print("Error: Username cannot exceed 50 characters.")
else:
    # Input for password
    password = input("Enter password: ")
 
    # Validate password
    special_symbols = "!@#$%^&*(),.?\":{}|<>"
    has_special_symbol = False
    has_number = False
    has_uppercase = False
    has_lowercase = False
    #Check the requirments of the Pasword (Iterates through each character in the password.
    #Checks if the character is a special symbol, a digit, an uppercase letter, or a lowercase letter, and 
    #sets the corresponding boolean variable to True if the condition is met.)
    for char in password:
        if char in special_symbols:
            has_special_symbol = True
        if char.isdigit():
            has_number = True
        if char.isupper():
            has_uppercase = True
        if char.islower():
            has_lowercase = True
	#Initializes password_error to False.
    #Checks if the password is less than 8 characters long. If it is, prints an error message and sets password_error to True.
    #Checks if the password lacks a special symbol, a number, an uppercase letter, or a lowercase letter. If any condition is not met, prints the corresponding 
    #error message and sets password_error to True
 
    password_error = False
    if len(password) < 8:
        print("Error: Password must be at least 8 characters long.")
        password_error = True
    if not has_special_symbol:
        print("Error: Password must contain at least one special symbol.")
        password_error = True
    if not has_number:
        print("Error: Password must contain at least one number.")
        password_error = True
    if not has_uppercase:
        print("Error: Password must contain at least one uppercase letter.")
        password_error = True
    if not has_lowercase:
        print("Error: Password must contain at least one lowercase letter.")
        password_error = True
 
    if not password_error:
        # Input for email
        email = input("Enter email: ")
 
        # Validate email
        if "@" not in email:
            print("Error: Email must contain '@' symbol.")
        else:
            user_domain = email.split('@')
            if len(user_domain) != 2:
                print("Error: Invalid email format.")
            else:
                user, domain = user_domain
                if not user.replace(".", "").isalnum():
                    print("Error: Email username must be alphanumeric.")
                else:
                    domain_parts = domain.split('.')
                    domain_error = False
                    if len(domain_parts) < 2:
                        print("Error: Email domain must have letters separated by '.'")
                        domain_error = True
                    for part in domain_parts:
                        if not part.isalpha():
                            print("Error: Email domain must contain only letters.")
                            domain_error = True
                            break
                    if domain.startswith('.') or domain.endswith('.'):
                        print("Error: Email domain cannot start or end with '.'")
                        domain_error = True
                    if not domain_error:
                        print("All inputs are valid.")