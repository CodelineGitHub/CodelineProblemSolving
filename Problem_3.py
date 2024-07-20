def display_right_triangle(n):
    for i in range(1, n + 1):
        print('1 ' * i)
 
def display_palindromic_triangle(n):
    for i in range(1, n + 1):
        # Generate left part of the palindromic line
        left_part = ''.join(str(x) for x in range(1, i + 1))
        # Generate right part of the palindromic line
        right_part = left_part[-2::-1]  # Get the reverse part excluding the middle element
        print(left_part + right_part)
 
def show_help():
    print("Help Menu:")
    print("A Palindromic Triangle is a triangle array of numbers where each row is a palindrome.")
    print("The first few lines of a Palindromic Triangle are:")
    print(" 1 ")
    print(" 121 ")
    print(" 12321 ")
    print(" 1234321 ")
    print("You can use this pattern to draw a Palindromic Triangle for any number of lines.")
 
def main():
    while True:
        print("\nMenu:")
        print("1. Display a right-triangle of ones")
        print("2. Display a Palindromic Triangle")
        print("3. Help")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            n = int(input("Enter the height of the right-triangle: "))
            display_right_triangle(n)
        elif choice == '2':
            n = int(input("Enter the height of the palindromic triangle: "))
            display_palindromic_triangle(n-1)
        elif choice == '3':
            show_help()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
 
if __name__ == "__main__":
    main()