def display_right_angle_triangle(lines):
    for i in range(1, lines + 1):
        print('1' * i)

def display_palindromic_triangle(lines):
    for i in range(1, lines + 1):
        left_side = ''.join(str(x) for x in range(1, i + 1))
        right_side = left_side[-2::-1]
        print(left_side + right_side)

def display_help():
    print("Menu Options:")
    print("1. Display a right-angle triangle of ones")
    print("   - Enter the number of lines you want the triangle to have.")
    print("2. Display a Palindromic Triangle")
    print("   - Enter the number of lines you want the palindromic triangle to have.")
    print("3. Help")
    print("   - Displays this help message.")
    print("4. Exit")
    print("   - Exits the program.")

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
            print("Invalid choice. Please select a valid option from the menu.")

if __name__ == "__main__":
    main()