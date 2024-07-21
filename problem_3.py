#Problem 3: Interactive Triangle Display
#Name: Juhaina Ahmed Al Siyabi
#Email: juhainaahmed123@icloud.com

def TriMaker():  # Main Program
    while True:
        # TriMaker Menu
        print("\nMenu:")
        print("1. Display a right-angle triangle of ones")
        print("2. Display a Palindromic Triangle")
        print("3. Help")
        print("4. Exit")
        choice = input("Enter your choice: ")

        # Run specific function based on user input
        if choice == '1':
            Right_Angle_TriMaker()
        elif choice == '2':
            Lines = int(input("Enter the number of lines for Palindromic Triangle: "))
            Palindromic_TriMaker(Lines)
        elif choice == '3':
            display_help()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Please choose one of the available options.")

def Right_Angle_TriMaker():
    print("Displaying a right-angle triangle of ones:") # Generate Right angle triangle 
    for i in range(1, 5):
        print("1 " * i)

def Palindromic_TriMaker(Lines):
    print("Displaying a Palindromic Triangle:") #Generating Palindromic Triangle with 1,11 being static and starting loop from line 3
    if Lines >= 1:
        print("1")
    
    if Lines >= 2:
        print("11")
    
    # Start of loops
    for i in range(3, Lines + 1):
        
        for j in range(1, i): # Print left half of the palindrome starting from 1 
            print(j, end="")
        
        for j in range(i - 2, 0, -1): # Print right half of the palindrome
            print(j, end="")
        
        print()

def display_help(): #Print Helpful details in choosing input 3
    print("""Help:
    A Palindromic Triangle is a triangular array of numbers where each row forms a palindrome.
    The first few Lines of a Palindromic Triangle are: 
    1
    11
    121
    12321
    1234321
    You can use this pattern to draw a Palindromic Triangle of any number of Lines.""")

if __name__ == "__main__":
    TriMaker()
