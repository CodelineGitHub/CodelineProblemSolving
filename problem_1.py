
# Function to validate the username
def validate_username(username):
    # Check if the username is empty or longer than 50 characters
    if not username or len(username) > 50:
        return "Username is invalid."
    return "Username is valid."

# Function to validate the password
def validate_password(password):
    # Check if the password meets the length requirement
    if len(password) < 8:
        return "Password is invalid."

    # Initialize variables to check requirements
    has_special_symbol = False
    has_digit = False
    has_upper = False
    has_lower = False

    # check each character in the password
    for char in password:
        # Check if character is a special symbol
        if char in "!@#$%^&*(),.?\":{}|<>":
            has_special_symbol = True
        # Check if character is a digit
        if char.isdigit():
            has_digit = True
        # Check if character is uppercase
        if char.isupper():
            has_upper = True
        # Check if character is lowercase
        if char.islower():
            has_lower = True

    # Validate all requirements
    if has_special_symbol and has_digit and has_upper and has_lower:
        return "Password is valid."
    else:
        return "Password is invalid."

# Function to validate the email
def validate_email(email):
    # Check if "@" is present in the email
    if "@" not in email:
        return "Email is invalid."
    
    # Split the email into two parts using "@" as separator
    parts = email.split("@")
    
    # Check if there are exactly two parts and both parts are non-empty
    if len(parts) != 2 or not parts[0] or not parts[1]:
        return "Email is invalid."
    
    # Validate the first part of the email
    for char in parts[0]:
        if not (char.isalnum() or char in ".-_+"):
            return "Email is invalid."
    
    # Split the domain part of the email by "."
    domain_parts = parts[1].split(".")
    
    # Check if the domain has at least two parts and all parts contain only letters
    if len(domain_parts) < 2 or not all(part.isalpha() for part in domain_parts):
        return "Email is invalid."
    
    return "Email is valid."

# Function to display the menu and get input from the user
def display_menu():
    # Get user input from user
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    email = input("Enter Email: ")
    
    # Validate input and print  results
    print(validate_username(username))
    print(validate_password(password))
    print(validate_email(email))

# Main block to run the program
if __name__ == "__main__":
    display_menu()
