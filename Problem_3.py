def display_right_angled_triangle_ones(size):
    for i in range(1, size + 1):
        print('1' * i)

def display_palindromic_triangle(size):
    for i in range(1, size + 1):
        num_str = ''.join(str(j) for j in range(1, i + 1))
        palindromic_str = num_str + num_str[-2::-1]
        print(palindromic_str)

def show_help():
    print("""
    Welcome to the Interactive Triangle Display Program!
    Here are the options you can choose:
    1. Display a right-angle triangle of ones:
       - You will be asked to enter the number of lines.
       - The triangle will be displayed with '1' characters.
    2. Display a Palindromic Triangle:
       - You will be asked to enter the number of lines.
       - The triangle will display lines with palindromic numbers.
    3. Help:
       - Displays this help information.
    4. Exit:
       - Exits the program.
    """)

def main():
    while True:
        print("""
        Menu:
        1. Display a right-angle triangle of ones
        2. Display a Palindromic Triangle
        3. Help
        4. Exit
        """)
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            size = int(input("Enter the number of lines: "))
            display_right_angled_triangle_ones(size)
        elif choice == '2':
            size = int(input("Enter the number of lines: "))
            display_palindromic_triangle(size)
        elif choice == '3':
            show_help()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
