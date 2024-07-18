"""
Author: Isra Musab Al Rasbi 
"""

'''
This function check if the name is valid or not
Input: name
Output: valid or invalid 
'''
def check_name(name):
    #if the length of the name is zero, this means there is no characters, hence return invalid
    if len(name) == 0:
        return "invalid"
    
    #if the length of the name greater than 50, the name is invalid 
    elif len(name) > 50:
        return "invalid"
    else:
        return "valid"
    
'''
This function check if the password is valid or not
Input: password
Output: valid or invalid 
'''
def check_password(password):
    #create a list for special symbol
    symbol=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "<", ">", "?", "/", "`", "~", "\\"]
    
    #create flags for the symbols, numbers, and uppercase and lowercase letters
    has_symbol= False
    has_num = False
    has_upp = False
    has_low = False
    
    #loop throgh the password to check if password contain the requirments 
    #if yes, change the flag from False to True 
    for i in password:
        #check for symbole from the list
        if i in symbol:
            has_symbol=True
        #check for numbers and letters 
        elif i.isdigit():
            has_num=True
        elif i.isupper():
            has_upp=True
        elif i.islower():
            has_low=True
            
        #check if all the flags are True, if yes then break, this avoid unnecessary iterations
        if has_symbol and has_num and has_upp and has_low:
            break
        
    #check if the password is valid or not
    #the length of the password should be greater or equal to 8 
    #and it should contain special symbol, numbers, and uppercase and lowercase characters
    if (len(password) >= 8) and (has_symbol and has_num and has_upp and has_low):
        return "valid"
    else:
        return("invalid")

'''
This function check if the email is valid or not
Input: email
Output: valid or invalid 
'''
def check_email(email):
    #define variables 
    at="@"
    dot="."
    
    #create flags 
    has_at=False
    has_dot=False
    has_char=False
    
    #loop throgh the email
    for i in email:
        #this check that there is @ 
        if i == at:
            has_at=True
            
            #if the above condtion is true, then slice after the @ and check if there is dot 
            after_at = email.split(at,1)[1]
            #check if there is dot 
            if dot in after_at:
                has_dot=True
                
                #check if there is characters before and after the dot
                #split the words based on the dot
                char = after_at.split(dot)
                #now check before and after the dot
                #there should be two parts, before which is char[0] and after which is char[1]
                if len(char) >= 2 and char[0].isalpha() and char[1].isalpha():
                    has_char = True
                else:
                    has_char = False
            #if there is no dot, then return false 
            else:
                has_char=False
            break 
        #if there is no @ then false
        else:
            has_char=False
  
    #check if email is valid
    if has_at and has_dot and has_char:
            return "valid"
    else:
        return "invalid"
    

#first ask the user to enter name, password, and email 
un = str(input("Username: "))
pw = str(input("Password: "))
mail = str(input("Email: "))

#second check the validity of the credentials by calling the functions 
name = check_name(un)
password = check_password(pw)
email = check_email(mail)

#print the results
print()
print(f"Username: {name}")
print(f"Password: {password}")
print(f"Email: {email}")