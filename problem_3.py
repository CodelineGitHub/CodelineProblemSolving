"""
@author: Shifa
Date: 20/7/2024
This program will display a menu containing an interactive triangle display choice.

"""
#Display menu
Exit = False
while not Exit:
    print("\nMenu:")
    print("1. Display a right-angle triangle of ones")
    print("2. Display a Palindromic Triangle")
    print("3. Help")
    print("4. Exit")
    
    #Enter the input
    print("Enter your choice: ", end="")
    choice=str(input())
    
    #Display right-angle triangle of ones
    if choice =="1":
        print("Enter number of lines: ", end="")
        lines = int(input())
        i = 1
        while i != (lines+1):
            print("1 " * i)
            i += 1 
            
    #Display Palindromic Triangle
    elif choice =="2":
        print("Enter number of lines: ", end="")
        lines = int(input())
        for i in range(1, lines+1):
            if i == 1:
                print("1")
            elif i == 2:
                print("11")
            else:
                for j in range(1, i):
                    print(j, end="")
                for j in range(i-2, 0, -1):
                    print(j, end="")
                print()
                
    #Display Help
    elif choice =="3":
        print("\nHelp:")
        print("A Palindromic Triangle is a triangular array of numbers with a palindrome in each row. A Palindromic Triangle's opening few lines are: ")
        print("1")
        print("11")
        print("121")
        print("12321")
        print("1234321")
        print("With any number of lines, a Palindromic Triangle can be created using this design.")
    
    #Exit the program
    elif choice =="4":
        print("Exiting the program")
        Exit = True
    else:
        print("Invalid choice")