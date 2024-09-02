def display_right_angle_triangle(n):
    """Display a right-angle triangle of ones."""
    for i in range(1, n + 1):
        print('1 ' * i)

def display_palindromic_triangle(n):
    """Display a palindromic triangle of numbers."""
    for i in range(1, n + 1):
        # Print increasing part
        for j in range(1, i + 1):
            print(j, end='')
        # Print decreasing part
        for j in range(i - 1, 0, -1):
            print(j, end='')
        print()

def show_help():
    """Display help information."""
    print("\nMenu Options:")
    print("1. Display a right-angle triangle of ones")
    print("   This option prints a right-angle triangle with ones.")
    print("2. Display a palindromic triangle")
    print("   This option prints a palindromic triangle with numbers in a symmetric pattern.")
    print("3. Help")
    print("   Shows this help menu.")
    print("4. Exit")
    print("   Exits the program.\n")

def main():
    """Main function to handle menu and user input."""
    while True:
        print("Menu:")
        print("1. Display a right-angle triangle of ones")
        print("2. Display a palindromic triangle")
        print("3. Help")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            try:
                n = int(input("Enter the number of lines: "))
                display_right_angle_triangle(n)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                
        elif choice == '2':
            try:
                n = int(input("Enter the number of lines: "))
                display_palindromic_triangle(n)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                
        elif choice == '3':
            show_help()
            
        elif choice == '4':
            print("Exiting the program.")
            break
            
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
        
        print()  # Print a newline for better readability

if __name__ == "__main__":
    main()