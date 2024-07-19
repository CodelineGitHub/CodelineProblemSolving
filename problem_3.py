def display_menu():
    print("\nMenu:")
    print("1. Display a right angle triangle of 1")
    print("2. Display a palindromic triangle")
    print("3. Help")
    print("4. Exit")

def right_angle_triangle(n):
    for i in range(1, n + 1):
        print("1 " * i)

def palindromic_triangle(n):
    for i in range(1, n + 1):
        # Left side numbers
        for j in range(1, i + 1):
            print(j, end="")
        # Right side numbers
        for j in range(i - 1, 0, -1):
            print(j, end="")
        print()

def help():
    print("\nHelp:")
    print("1. Display a right angle triangle of 1: This option displays a right-angle triangle made of the number 1.")
    print("   Example for n=4:")
    print("   1")
    print("   1 1")
    print("   1 1 1")
    print("   1 1 1 1\n")
    print("2. Display a palindromic triangle: This option displays a triangle where each row forms a palindrome.")
    print("   Example for n=4:")
    print("   1")
    print("   121")
    print("   12321")
    print("   1234321")

def main():
    while True:
        display_menu()
        try:
            choice = int(input("\nEnter your choice (1-4): "))
            if choice == 1:
                n = int(input("Enter the number of rows for the right angle triangle: "))
                right_angle_triangle(n)
            elif choice == 2:
                n = int(input("Enter the number of rows for the palindromic triangle: "))
                palindromic_triangle(n)
            elif choice == 3:
                help()
            elif choice == 4:
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
