def display_right_angle_triangle(n):
    for i in range(1, n + 1):
        print('1' * i)


def display_palindromic_triangle(n):
    for i in range(1, n + 1):
        left_part = ''.join(str(x) for x in range(1, i + 1))
        right_part = ''.join(str(x) for x in range(i - 1, 0, -1))
        print(left_part + right_part)


def display_help():
    print("Help:\nA Palindromic Triangle is a triangular array of numbers where each row forms a palindrome.")
    print("The first few lines of a Palindromic Triangle are:\n1\n121\n12321\n1234321\n123454321")
    print("You can use this pattern to draw a Palindromic Triangle for any number of lines.")


def main_menu():
    while True:
        print("\nMenu:")
        print("1. Display a right-angle triangle of ones")
        print("2. Display a Palindromic Triangle")
        print("3. Help")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            n = int(input("Enter the number of lines: "))
            display_right_angle_triangle(n)
        elif choice == '2':
            n = int(input("Enter the number of lines: "))
            display_palindromic_triangle(n)
        elif choice == '3':
            display_help()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main_menu()