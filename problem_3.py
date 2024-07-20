def display_right_angle_triangle(lines):
    for i in range(1, lines + 1):
        print('1 ' * i)

def display_palindromic_triangle(lines):
    for i in range(1, lines + 1):
        # Print leading spaces
        for j in range(lines - i):
            print(' ', end='')

        # Print increasing part of the pattern
        for j in range(1, i + 1):
            print(j, end='')

        # Print decreasing part of the pattern
        for j in range(i - 1, 0, -1):
            print(j, end='')

        print()

def display_help():
    print("A Palindromic Triangle is a triangular array of numbers where each row forms a palindrome.")
    print("The first few lines of a Palindromic Triangle are:")
    print("1")
    print("11")
    print("121")
    print("12321")
    print("1234321")
    print("You can use this pattern to draw a Palindromic Triangle for any number of lines.")

def main():
    while True:
        print("\nMenu:")
        print("1. Display a right-angle triangle of ones")
        print("2. Display a Palindromic Triangle")
        print("3. Help")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            lines = int(input("Enter the number of lines: "))
            display_right_angle_triangle(lines)
        elif choice == 2:
            lines = int(input("Enter the number of lines: "))
            display_palindromic_triangle(lines)
        elif choice == 3:
            display_help()
        elif choice == 4:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
