In [11]:
def login():
  username=input("Username:")
  password=input("Password:")
  email=input("Email:")

if not username or len(username)>50:
  print("Username is invalid")
else:
  print("Username is valid")


if len(password)<8 or not (r'[!@
