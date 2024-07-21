
def displayPalindromicTriangle(lines):
    for i in range(1, lines + 1):
       
        left_side = ''.join(str(num) for num in range(1, i + 1))
        
        right_side = left_side[:-1][::-1]
        
        print(left_side + right_side)
    print()
    
    
    
def displayRightTriangle(lines):
    for i in range(1, lines + 1):
        print('1 ' * i)
    print()



def displayHelp():
    print("A palindromic Triangle is a triangular array of numbers where each row forms a palindrome.")
    print("The first few lines of a palindromic triangle are:")
    print("1")
    print("11")
    print("121")
    print("12321")
    print("1234321")
    print("You can use this pattern to draw a palindromic triangle for any number of lines.\n")

def main():
    while True:
        print("Menu:")
        print("1. Display a right-angle triangle of ones")
        print("2. Display a Palindromic Triangle")
        print("3. Help")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            lines = int(input("Enter the number of lines: "))
            displayRightTriangle(lines)
        elif choice == '2':
            lines = int(input("Enter the number of lines: "))
            displayPalindromicTriangle(lines)
        elif choice == '3':
            displayHelp()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


main()

