
"""
@author: Shifa
Date: 20/7/2024
This program will ask the user to enter: a username, password, and email, 
then check each input to see if it is valid or not.

"""
#Import library
import re

#Enter and check Username
print("Enter your:")
print("Username:", end=" " )
username = str(input())
if username =="" or len(username) > 50:
    user_output = "Username is invalid"
else:
    user_output = "Username is valid"

#Enter and check Password
print("Password:" , end=" "  )
password = input()
specialSym = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
#Check length
if len(password) < 8 :
    pass_output = "Password is invalid"
#Check special symbol
elif (specialSym.search(password) == None):
    pass_output = "Password is sym invalid"
#Check Digit
elif not any(char.isdigit() for char in password):
    pass_output = "Password is invalid"
#Check characters
elif not any(char.isalpha() for char in password):
    pass_output = "Password is invalid"
#Check Upper case
elif not any(char.isupper() for char in password):
    pass_output = "Password is invalid"
#Check Lower case
elif not any(char.islower() for char in password):
    pass_output = "Password is invalid"
else:
    pass_output = "Password is valid"

#Enter and check email
print("Email:" , end=" "  )
email = input()

#Check @ symbol
if "@" not in email:
    email_output = "Email is invalid"
else:
    for char in email:
        if char =="@":
            index = email.index(char)
            email_p1 = email[:index]
            email_p2 = email[index+1:]
            break
    #check alphanumeric before @
    if not any(char.isalnum() for char in email_p1):
        email_output = "Email is invalid"
    #check alphanumeric after @
    elif not any(char.isalnum() for char in email_p2):
        email_output = "Email is invalid"
    #check dot(.) after @
    elif "." not in email_p2:
        email_output = "Email is invalid"
  
    else:
        email_output = "Email is valid"  
    
#Display output
print("\nThe output:")
print(user_output)
print(pass_output)
print(email_output)