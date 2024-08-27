def right_angle_triangle_ones(n):
    for i in range(1, n + 1):
        print("1" * i)


def palindromic_triangle(n):
    for i in range(1, n + 1):
        # Create the increasing part of the pattern
        num_str = ''.join(str(x) for x in range(1, i + 1))
        # Print the full palindrome by appending the reversed part without the first character
        print(num_str + num_str[::-1][1:])


def display_help():
    help_message = """
Help:
A Palindromic Triangle is a triangular array of numbers where each row forms a palindrome.
The first few lines of a Palindromic Triangle are:
1
121
12321
1234321
You can use this pattern to draw a Palindromic Triangle for any number of lines.
"""
    print(help_message)


def main():
    while True:
        print("Menu:")
        print("1. Display a right-angle triangle of ones")
        print("2. Display a Palindromic Triangle")
        print("3. Help")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            n = int(input("Enter the number of lines: "))
            right_angle_triangle_ones(n)
        elif choice == 2:
            n = int(input("Enter the number of lines: "))
            palindromic_triangle(n)
        elif choice == 3:
            display_help()
        elif choice == 4:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
