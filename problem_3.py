def display_right_angle_triangle(n):
    for i in range(1, n + 1):
        print('1 ' * i)

def display_palindromic_triangle(n):
    for i in range(1, n + 1):
        # Left side
        for j in range(1, i + 1):
            print(j, end="")
        # Right side
        for j in range(i - 1, 0, -1):
            print(j, end="")
        print()

def show_help():
    print("Help Menu:")
    print("A Palindromic Triangle is a triangular array of numbers where each row forms a palindromic.")
    print("The first few lines of Plindromic Triangle are:")
    print("1")
    print("11")
    print("121")
    print("12321")
    print("1234321")
    print("You can use this pattren to draw a Plindromic Triangle for any number of lines.")
    

def main():
    while True:
        print("\nMenu:")
        print("1. Display a right-angle triangle of ones")
        print("2. Display a Palindromic Triangle")
        print("3. Help")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice (1-4): "))
            if choice == 1:
                n = int(input("Enter the number of rows for the right-angle triangle: "))
                display_right_angle_triangle(n)
            elif choice == 2:
                n = int(input("Enter the number of rows for the palindromic triangle: "))
                display_palindromic_triangle(n)
            elif choice == 3:
                show_help()
            elif choice == 4:
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":

    main()
