import re
import string
username = ''
password = ''
email = ''
# this as argument in compile method
regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

# for validating an Email
regex2 = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'


def inputInfo():
    global username ,password ,email 
    username = input('Username: ')
    password = input('Passwrod: ')
    email = input('Email: ')

def validateInfo():
    if 1 <= len( username.strip())  < 50:
        print('Username is valid')
    else:
        print('Username is invalid')
    
    if len( password.strip()) >= 8 and bool(re.search(r'\d',password)) and  (not (regex.search(password) == None) ) and bool(re.search(r'[A-Z]', password)) and bool(re.search(r'[a-z]', password)):
        print('Password is valid')
    else:
        print('Password is invalid')
    if (re.fullmatch(regex2,email)):
        print('Email is valid')
    else:
        print('Email is invalid')
    
    
inputInfo()
validateInfo()