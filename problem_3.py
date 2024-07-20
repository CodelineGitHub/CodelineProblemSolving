print("Menu:\n1. Display a right triangle of ones\n"
     "2. Display a Palindromic Triangle\n3. Help\n4. Exit\n")
num = int(input("Enter your choice: "))
if num == 1:
    n1 = int(input("Enter the number of lines: "))
    for r in range(1, n1+1):
       for s in range(1, (r+1)):
           print("1", end=" ")
       for m in range(1, (n1 - 1)+1):
           print(" ", end="")
       print()
#----------------------------------------------------------------------------------------------
elif num == 2:
    n2 = int(input("Enter the number of lines: "))
    for r in range(1, n2+1):
        for s in range(1, r+1):
            print(s, end=" ")
        for m in range(s - 1,0,  -1):
            print(m, end=" ")
        print()
#----------------------------------------------------------------------------------------------
elif num == 3:
    n3 = ("Help:\nThis program can be used to draw two types of triangles:\n\n"
           "The first Triangle is a right-angel triangle of ones.\n"
           "1        \n1 1     \n1 1 1   \n1 1 1 1\n"
           "You choose this type of Triangle by typing (1) in the Menu.\n"
           "You can choose specify the number lines needed.\n\n"
           "The second Triangle is a Palindromic Triangle.\n"
           "1\n1 2 1\n1 2 3 2 1\n1 2 3 4 4 3 2 1\n"
           "You choose this type of Triangle by typing (2) in the Menu.\n"
           "You can choose specify the number lines needed.\n")
    print(n3)
#----------------------------------------------------------------------------------------------
elif num == 4:
    print("Exiting the program.")
else:
    print("Please choose a number from the Menu...")

