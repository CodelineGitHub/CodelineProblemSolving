import re
 
def username():
 while True:
    user_name = input("User_name:")
    if not (user_name):
      print("Error,The username should not be empty")
      continue
    if len(user_name) > 50:
      print("Error,It should not exceed more than 50 characters")
      continue
    else:
      print(f"Username {user_name} is valid")
    break
  
def password():
  while True:
    password=input("Password:")
    if (len(password))<8:
       print("Password must be at least 8 characters",password)
       continue
    if not re.search(r"[!@#$%^&*(),.?:{}|<>]",password):
     print("Password must contain at least one special symbol")
     continue
    if not re.search(r"[A-Z]",password) and not re.search(r"[a-z]",password):
     print("Password must contain at least one uppercase and  lowecase etter")
     continue
    else:
       print(f"Password {password} is valid")
    break
def email():
   while True:
    email=input("Email:")
    if "@" not in email:
      print("The email should have “@” symbol.") 
      continue
    if not re.match(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]", email):
     print("It should have alphanumeric characters before and after the @ symbol")    
     continue
    else:
      print(f"Email {email} is valid")
    break
   

 
username()
password()
email()
 

 
