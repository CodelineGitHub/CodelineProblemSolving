
# solution problem three
def display_right_angle_triangle(lines):
    for i in range(1, lines + 1):
        print("1" * i)

def display_palindromic_triangle(lines):
    for i in range(1, lines + 1):
        left = ''.join(str(x) for x in range(1, i + 1))
        right = ''.join(str(x) for x in range(i - 1, 0, -1))
        print(left + right)

def display_help():
    print("Help Menu:")
    print("1. Display a right-angle triangle of ones: Displays a right-angle triangle with the specified number of lines.")
    print("2. Display a Palindromic Triangle: Displays a palindromic triangle with the specified number of lines.")
    print("3. Help: Displays this help menu.")
    print("4. Exit: Exits the program.")

def main():
    while True:
        print("\nMenu:")
        print("1. Display a right-angle triangle of ones")
        print("2. Display a Palindromic Triangle")
        print("3. Help")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            lines = int(input("Enter the number of lines: "))
            display_right_angle_triangle(lines)
        elif choice == "2":
            lines = int(input("Enter the number of lines: "))
            display_palindromic_triangle(lines)
        elif choice == "3":
            display_help()
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()














