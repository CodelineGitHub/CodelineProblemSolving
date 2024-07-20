def display_right_angle_triangle():
    rows = int(input("Enter the number of rows for the right-angled triangle: "))
    for i in range(1, rows + 1):
        print('*' * i)

def display_alternating_triangle():
    rows = int(input("Enter the number of rows for the alternating triangle: "))
    for i in range(1, rows + 1):
        if i % 2 == 0:
            print('+' * i)
        else:
            print('*' * i)

def display_help():
    print("""
Menu options:
1. Display a right-angled triangle
2. Display an alternating triangle
3. Help (display menu options)
4. Exit
    """)

def main():
    while True:
        print("\nMenu:")
        print("1. Display a right-angled triangle")
        print("2. Display an alternating triangle")
        print("3. Help")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            display_right_angle_triangle()
        elif choice == '2':
            display_alternating_triangle()
        elif choice == '3':
            display_help()
        elif choice == '4':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()

