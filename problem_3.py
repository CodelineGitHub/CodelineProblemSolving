# Function to display a right-angle triangle of ones
def display_right_angle_triangle(lines):
    for i in range(1, lines + 1):
        print("1" * i)

# Function to display a Palindromic Triangle
def display_palindromic_triangle(lines):
    for i in range(1, lines + 1):
        # print the increasing numbers
        for j in range(1, i + 1):
            print(j, end="")
        # print the decreasing numbers
        for j in range(i - 1, 0, -1):
            print(j, end="")
        # Move to the next line
        print()

# Function to display help option
def display_help():
    print("Help:")
    print("A Palindromic Triangle is a triangular array of numbers where each row forms a palindrome.")
    print("The first few lines of a Palindromic Triangle are:")
    print("1")
    print("11")
    print("121")
    print("12321")
    print("1234321")
    print("\nYou can use this pattern to draw a Palindromic Triangle for any number of lines.")

# Function to display  menu 
def display_menu():
    print("\nMenu:")
    print("1. Display a right-angle triangle of ones")
    print("2. Display a Palindromic Triangle")
    print("3. Help")
    print("4. Exit")


if __name__ == "__main__":
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            lines = int(input("Enter the number of lines: "))
            display_right_angle_triangle(lines)
        
        elif choice == '2':
            lines = int(input("Enter the number of lines: "))
            display_palindromic_triangle(lines)
        
        elif choice == '3':
            display_help()
        
        elif choice == '4':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
