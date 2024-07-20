def print_menu():
    print("\nMenu:")
    print("1. Display a right-angle triangle of ones")
    print("2. Display a Palindromic Triangle")
    print("3. Help")
    print("4. Exit")


def get_num_of_lines():
    num_of_lines = input("Enter the number of lines: ")

    while not num_of_lines.isdigit() or int(num_of_lines) < 1:
        print("The number of lines should greater than 0.")
        num_of_lines = input("Enter the number of lines: ")

    return int(num_of_lines)


def right_angle_triangle():
    num_of_lines = get_num_of_lines()

    for i in range(1, num_of_lines + 1):
        print("1" * i)


def palindromic_triangle():
    num_of_lines = get_num_of_lines()

    for i in range(1, num_of_lines + 1):
        first_half = ''.join(str(j) for j in range(1, i + 1))
        # first half + the reverse of the first half excluding the last digit
        print(first_half + first_half[-2::-1])


def display_help():
    print("\nHelp:")
    print("A Palindromic Triangle is a triangular array of numbers where each row forms a palindrome.")
    print("The first few lines of a Palindromic Triangle are:")
    print("1")
    print("121")
    print("12321")
    print("1234321")
    print("You can use this pattern to draw a Palindromic Triangle for any number of lines.")


def main():
    while True:
        print_menu()
        choice = input("Enter your choice: ")

        # Check that the entered value is valid
        while not choice.isdigit() or int(choice) < 1 or int(choice) > 4:
            print("The entered choice must be an integer between 1 and 4.")
            choice = input("Enter your choice: ")

        if choice == "1":
            right_angle_triangle()
        elif choice == "2":
            palindromic_triangle()
        elif choice == "3":
            display_help()
        else:
            print("Exiting the program.")
            exit()


if __name__ == "__main__":
    main()
