def DisplayMenu():
    print("Menu:")
    print("1. Display a right-angle triangle of ones")
    print("2. Display a Palindromic Triangle")
    print("3. Help")
    print("4. Exit")

def RightAngleTriangleOfOnes(x):
    for y in range(1, x + 1):
        print('1 ' * y)

def PalindromicTriangle(x):
    for y in range(1, x + 1):

        for w in range(1, y+1):
            print(w, end='')

        for w in range(y-1, 0, -1):
            print(w, end='')
        print()

def help_menu():
    print("Help:")
    print("A Palindromic Triangle is a triangular array of numbers where each row forms a palindrome.")
    print("The first few lines of a Palindromic Triangle are:")
    print("1")
    print("11")
    print("121")
    print("12321")
    print("1234321")
    print("You can use this pattern to draw a Palindromic Triangle for any number of lines")

def main():
    while True:
        DisplayMenu()
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            n = int(input("Enter the number of rows: "))
            RightAngleTriangleOfOnes(n)
        elif choice == '2':
            n = int(input("Enter the number of rows: "))
            PalindromicTriangle(n)
        elif choice == '3':
            help_menu()
        elif choice == '4':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice, please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()

