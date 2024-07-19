def display_right_angle_triangle(rows):
    for i in range(1, rows + 1):
        print('1 ' * i)

def display_palindromic_triangle(rows):
    for i in range(1, rows + 1):
        left_part = ''.join(str(x) for x in range(1, i + 1))
        right_part = left_part[::-1][1:]
        print(left_part + right_part)

def display_help():
    print("Menu Options:")
    print("1. Display a right-angle triangle of ones.")
    print("2. Display a palindromic triangle.")
    print("3. Help ")
    print("4. Exit ")

def main():
    while True:
        print("\nMenu:")
        print("1. Display a right-angle triangle of ones")
        print("2. Display a palindromic triangle")
        print("3. Help")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            try:
                rows = int(input("Enter the number of rows: "))
                if rows <= 0:
                    print("Please enter a positive number of rows.")
                    continue
                display_right_angle_triangle(rows)
            except ValueError:
                print("Invalid input. Please enter a valid positive integer for the number of rows.")

        elif choice == "2":
            try:
                rows = int(input("Enter the number of rows: "))
                if rows <= 0:
                    print("Please enter a positive number of rows.")
                    continue
                display_palindromic_triangle(rows)
            except ValueError:
                print("Invalid input. Please enter a valid positive integer for the number of rows.")

        elif choice == "3":
            display_help()

        elif choice == "4":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice, please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
