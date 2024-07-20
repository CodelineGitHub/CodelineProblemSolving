# importing the re module to use the re.search method check the availability of a specific value
import re
# importing the validate_email to use the validate_email method which used to check the validity of an email
from validate_email import validate_email
name = input("Username: ")
paswd = input("Password: ")
email = input("Email: ")
#----------------------------------------------------------------------------------------------
##Code for Name checking
while True:
    ## if the lenght of the username is more than 50 it will return an erorr messagge.
    if (len(name) > 50):
        print("Username is invalid")
        break
    ## if input is blank it will return an erorr messggae.
    elif not (name):
        print("Username is invalid")
        break
    else:
        print("Username is valid")
        n = False
        break
#----------------------------------------------------------------------------------------------
##Code for Password checking
p = True
while p:
    ## if the password is less than 8 characters it will return an error message
    if (len(paswd) < 8):
        print("Password is invalid")
        break
    ## if the password don't cotain at least spicial character it will return an error message
    elif not re.search("[!#$%&@*+=]", paswd):
        print("Password is invalid")
        break
    ## if the password don't cotain at least one number it will return an error message
    elif not re.search("[0-9]", paswd):
        print("Password is invalid")
        break
    ## if the password don't cotain at least one lowercase letter it will return an error message
    elif not re.search("[a-z]", paswd):
        print("Password is invalid")
        break
    ## if the password don't cotain at least one uppercase latter it will return an error message
    elif not re.search("[A-Z]", paswd):
        print("Password is invalid")
        break
    ##else the password will be valid
    else:
        print("Password is valid")
        p = False
        break
#----------------------------------------------------------------------------------------------
##Code for Email checking
##using the validate_email method we can use it for valid the email easily
val_email = validate_email(email)
if val_email:
    print("Email is valid")
else:
    print("Email is invalid")




