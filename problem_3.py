def display_menu():
    print("\nMenu:")
    print("1. Display a right-angle triangle of ones")
    print("2. Display a Palindromic Triangle")
    print("3. Help")
    print("4. Exit")

def display_right_angle_triangle(lines):
    for i in range(1, lines + 1):
        print("1" * i)

def display_palindromic_triangle(lines):
    for i in range(1, lines + 1):
        left_half = ''.join(str(j) for j in range(1, i + 1))
        right_half = left_half[-2::-1]  # reverse left_half except the last character
        print(left_half + right_half)

def show_help():
    print("\nHelp:")
    print("1. Display a right-angle triangle of ones: Prompts for the number of lines and displays a triangle of ones.")
    print("2. Display a Palindromic Triangle: Prompts for the number of lines and displays a palindromic triangle.")
    print("3. Help: Displays this help message.")
    print("4. Exit: Exits the program.")

def main():
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
            show_help()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
