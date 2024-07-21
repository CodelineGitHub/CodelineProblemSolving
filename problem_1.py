def validateUsername(user):
    if not user:
        return 0
    if len(user) > 50:
        return 0
    return None

def validatePassword(password):
    special_symbols = "!@#$%^&*(),.?\":{}|<>"
    
    specialSymbol = any(char in special_symbols for char in password)
    number = any(char.isdigit() for char in password)
    uppercase = any(char.isupper() for char in password)
    lowercase = any(char.islower() for char in password)
    
    if len(password) < 8:
        return 0
    if not specialSymbol:
        return 0
    if not  number:
        return 0
    if not uppercase:
        return 0
    if not lowercase:
        return 0
    return None

def validateEmail(email):
    
    if "@" not in email:
        return 0
    parts = email.split("@")
    if len(parts) != 2:
        return 0
    
    localPart, domainPart = parts
    if not localPart.isalnum():
        return 0
    
    domainParts = domainPart.split(".")
    if len(domainParts) < 2:
        return 0
    if not all(part.isalpha() for part in domainParts):
        return 0
    
    return None

def main():
   
    username = input("Username: ")
    password = input("Password: ")
    email = input("Email: ")
    
    
    usernamError = validateUsername(username)
    passwordError = validatePassword(password)
    emailError = validateEmail(email)
    
   
    if usernamError == 0:
        print("Username is invalid")
    else:
        print("Username is valid")
    
    if passwordError == 0:
        print("Password is invalid")
    else:
        print("Password is valid")
    
    if emailError == 0:
        print("Email is invalid")
    else:
        print("Email is valid")

main()
