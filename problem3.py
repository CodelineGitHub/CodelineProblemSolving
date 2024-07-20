"""
Author: Isra Musab Al Rasbi 
"""
import sys
'''
This function print right angled triangle of ones 
Input: number of lines 
Output: right angled triangle of ones 
'''
def opt1(n):
    #loop through the number of lines 
    for i in range(n):
        #print the triangle and increase by 1 
        print("1" * (i+1))

'''
This function print palindromic triangle 
Input: number of lines 
Output:palindromic triangle 
'''
def opt2(n):
    #loop through the number of lines starting at 1 
    for i in range(1 , n+1):
        #define variables 
        #the val variable will generate the palindromic sequence
        val = 0
        #calculate the number of numbers in lines 
        num = 2 * i - 1
        
        #loop through the numbers within the line
        for j in range(1, num+1):
            #generate the palindromic sequence
            if(j<=i):
                val=val+1
            else:
                val=val-1
            #print the palindromic sequence without starting a new line
            print(val,end="")
        print()

            
'''
This function print info about the palindromic triangle 
Input:
Output: info
'''
def opt3():
    print("Help:\nA Palindromic Triangle is a triangular array of numbers where each row forms a palindrome.")
    print("The first few lines of a Palindromic Triangle are:")
    opt2(5)
    print("You can use this pattern to draw a Palindromic Triangle for any number of lines.")

'''
This function exit the program
Input:
Output: exit message 
'''
def opt4():
    print("Exiting the program.")
    #exit the program, use the exit function form sys library
    sys.exit()


#display the menu and ask the user to enter choice
while True:
    print()
    print("Menu:") 
    print("1. Display a right-angle triangle of ones")
    print("2. Display a Palindromic Triangle")
    print("3. Help")
    print("4. Exit")
    #add error handling
    try:
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            try:
                lines = int(input("Enter the number of lines: "))
                opt1(lines)
            except ValueError:
                print("Error!! please enter a number")
                
        elif choice == 2:
            try:
                lines = int(input("Enter the number of lines: "))
                opt2(lines)
            except ValueError:
                print("Error!! please enter a number")
                
        elif choice == 3:
            opt3()
            
        elif choice == 4:
            opt4()
            
        else:
            print("Invalid choice")
    
    except ValueError:
        print("Invalid input")

