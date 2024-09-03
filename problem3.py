def display_right_angle_triangle(rows):
    for i in range(1, rows + 1):
        # Print '1' for each position in the row
        print('1 ' * i)

def display_palindromic_triangle(rows):
    for i in range(1, rows + 1):
        # Create the left half of the palindrome
        left_half = ''.join(str(num) for num in range(1, i + 1))
        # Create the right half of the palindrome
        right_half = left_half[::-1][1:]  # Exclude the middle character
        # Print the palindromic row
        print(left_half + right_half)

def display_help():
    print("Help Menu:")
    print("1. Display a right-angle triangle of ones: This will print a right-angle triangle with all ones.")
    print("2. Display a palindromic triangle: This will print a triangle where each row forms a palindrome.")
    print("3. Help: Displays this help menu.")
    print("4. Exit: Exits the program.")

def main():
    while True:
        print("\nTriangle Display Menu:")
        print("1. Display a right-angle triangle of ones")
        print("2. Display a palindromic triangle")
        print("3. Help")
        print("4. Exit")

        choice = int(input("Enter your choice (1-4): "))

        if choice == 1:
            rows = int(input("Enter the number of rows: "))
            if rows <= 0:
                print("Number of rows must be positive.")
                continue
            display_right_angle_triangle(rows)
        elif choice == 2:
            rows = int(input("Enter the number of rows: "))
            if rows <= 0:
                print("Number of rows must be positive.")
                continue
            display_palindromic_triangle(rows)
        elif choice == 3:
            display_help()
        elif choice == 4:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
