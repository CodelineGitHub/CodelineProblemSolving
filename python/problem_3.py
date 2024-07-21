def display_right_angle_triangle(lines):
    for i in range(1, lines + 1):
        print("1" * i)

def display_palindromic_triangle(lines):
    for i in range(1, lines + 1):
        # Print leading spaces
        print(" " * (lines - i), end="")
        # Print ascending numbers
        for j in range(1, i + 1):
            print(j, end="")
        # Print descending numbers
        for j in range(i - 1, 0, -1):
            print(j, end="")
        print()  # Newline after each row
        
        
def show_help():
    print("Help Menu")
    print("1. Display a right-angle triangle of ones: Prints a triangle with the given number of lines where each line has ones.")
    print("2. Display a Palindromic Triangle: Prints a triangle with palindromic numbers for the given number of lines.")
    print("3. Help: Displays this help menu.")
    print("4. Exit: Exits the program.")

def main():
    while True:
        print("\nMenu:")
        print("1. Display a right-angle triangle of ones")
        print("2. Display a Palindromic Triangle")
        print("3. Help")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            lines = int(input("Enter the number of lines: "))
            display_right_angle_triangle(lines)
        elif choice == '2':
            lines = int(input("Enter the number of lines: "))
            display_palindromic_triangle(lines)
        elif choice == '3':
            show_help()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
