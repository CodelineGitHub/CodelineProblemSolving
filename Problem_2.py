def display_right_angled_triangle(size):
    for i in range(1, size + 1):
        print('*' * i)

def display_alternating_triangle(size):
    for i in range(1, size + 1):
        if i % 2 == 0:
            print('#' * i)
        else:
            print('*' * i)

def show_help():
    print("""
    Welcome to the Interactive Triangle Display Program!
    Here are the options you can choose:
    1. Display a right-angled triangle:
       - You will be asked to enter the size of the triangle.
       - The triangle will be displayed with '*' characters.
    2. Display an alternating triangle:
       - You will be asked to enter the size of the triangle.
       - The triangle will display alternating lines of '*' and '#' characters.
    3. Help:
       - Displays this help information.
    4. Exit:
       - Exits the program.
    """)

def main():
    while True:
        print("""
        Menu:
        1. Display a right-angled triangle
        2. Display an alternating triangle
        3. Help
        4. Exit
        """)
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            size = int(input("Enter the size of the triangle: "))
            display_right_angled_triangle(size)
        elif choice == '2':
            size = int(input("Enter the size of the triangle: "))
            display_alternating_triangle(size)
        elif choice == '3':
            show_help()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
