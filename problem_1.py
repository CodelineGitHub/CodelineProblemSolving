#Problem 1: User Login Validation
#Name: Juhaina Ahmed Al Siyabi
#Email: juhainaahmed123@icloud.com

import re

def UserAcc(): #Main Program
    #User inputs its details
    username = input("Enter Username: ")  # User types their username
    password = input("Enter Password: ")  # User types their password
    email = input("Enter Email: ")  # User types their email

    #Input validation with required criteria (If field output is invalid the message appears beside invalid input)
    is_username_valid, username_msg = validate_username(username)
    is_password_valid, pwd_msg = validate_pwd(password)
    is_email_valid, email_msg = validate_email(email)

    #user Input validation
    #-------------------Username------------------
    if is_username_valid: 
        print("Username is valid")
    else:
        print(f"Username is invalid ({username_msg})")
    #-------------------Password------------------
    if is_password_valid: 
        print("Password is valid")
    else:
        print(f"Password is invalid ({pwd_msg})")
    #-------------------Email---------------------
    if is_email_valid: 
        print("Email is valid")
    else:
        print(f"Email is invalid ({email_msg})")

#Username validation       
def validate_username(username):
    if not username:
        return False, "Username should not be empty." #If Empty
    if len(username) > 50:
        return False, "Username should not exceed 50 characters." #If More than 50 Chars
    if not re.match("^[a-zA-Z]+$", username):
        return False, "Username should contain only letters." #If includes numerical/special Chars
    return True, ""

#Password validation
def validate_pwd(password):
    if not password:
        return False, "Password should not be empty." #If Empty
    if len(password) < 8:
        return False, "Password must be at least 8 characters long." #If Length is < 8
    if not re.search("[0-9]", password):
        return False, "Password must contain at least one number." #If number not included
    if not re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Password must contain at least one special character." #If Special char not included
    if not re.search("[A-Z]", password):
        return False, "Password must contain at least one uppercase letter." #If Upper-case not included
    if not re.search("[a-z]", password):
        return False, "Password must contain at least one lowercase letter." #If Lower-case not included
    return True, ""

#Email validation
def validate_email(email):
    if not email:
        return False, "Email should not be empty." #If Empty
    if "@" not in email:
        return False, "Email should contain '@' symbol." #If @ Symbol not included
    parts = email.split("@")
    if len(parts) != 2:
        return False, "Email should contain only one '@' symbol." #If more than @ is included
    if not re.search("[a-zA-Z0-9]", parts[0]) or not parts[0]:
        return False, "Email should have alphanumeric characters before '@' symbol." #If Letters/Numbers are not included
    domain_part = parts[1]
    if not domain_part.endswith(".com"): #If Email not ending with '.com' (Strictly with .com)
        return False, "Email should end with '.com'."
    return True, ""

if __name__ == "__main__":
    UserAcc()
