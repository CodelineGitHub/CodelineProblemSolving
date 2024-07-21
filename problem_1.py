In [11]:
def login():
  username=input("Username:")
  password=input("Password:")
  email=input("Email:")

if not username or len(username)>50:
  print("Username is invalid")
else:
  print("Username is valid")

if len(password)<8 or not (r'[!@#$%^&*(),.|<>]',password) or not (r'[A-Z]',password) or not (r'[a-z]',password) or not (r'[0-9]',password):
         print("Password is invalid")
    else:
        print("Password is valid")


 if (r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
          print("Password is invalid")

    else:

        print("Password is valid")



    if (r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        print("Email is valid")
    else:
        print("Email is invalid")

login()
