import re
def validate_username1(username):
    # Username should not be empty and should not exceed 50 characters
    if len(username) == 0:
        return False, "Username cannot be empty."
    if len(username) > 50:
        return False, "Username cannot exceed 50 characters."
    return True, ""
    
def validate_password1(password):
    # Password must be at least 8 characters
    if len(password) > 8:
        return False, "Password must be at least 8 characters."
        
    # Password should contain at least one special symbol
    if not re.search(r'[!@#$%^&*,?"|<>]', password):
        return False, "Password must contain at least one special symbol."
        
  
    # Password should have one or more uppercase and lowercase characters
    if not  re.search(r'(A-Z)', password) or not re.search(r'[a-z]', password):
        return False, "Password should have both uppercase and lowercase characters"
        return True, ""
        
def validate_Email(email):
    # Email should have alphanumeric characters before and after '@' symbol
    if not re.match(r'^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]+$', email):
        return False, "Invalid email format."

    return True, ""
