while True:
    
    username = input("Username: ")
    password = input("Password: ")
    email = input("Email: ")
    
    if username and len(username) < 50:
         print("Username is valid.")
    else:
         print("Username is invalid.")
    
    if (len(password)>= 8 and
    any(i in '~!@#$%^&*()|[]?<>,\/;{}' for i in password ) and 
    any(i.isdigit() for i in password ) and 
    any(i.isupper() for i in password) and
    any(i.islower() for i in password)):
        print("Password is valid.")
    else:
        print("Password is invalid.")
        
    if "@" in email and "." in email:
        x = email.split("@")
        if len(x)==2 and x[0] and x[1]:
            domain = x[1].split(".")
            if len(domain)==2 and domain[0] and domain[1]:
                print("Email is valid.")
            
    else:
        print("Email is invalid.")