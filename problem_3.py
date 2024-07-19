def display_right_angle_triangle(num_lines):
    for i in range(1, num_lines + 1):
        print('1' * i)

def display_palindromic_triangle(num_lines):
    for i in range(1, num_lines + 1):
        # Create the first half of the palindrome
        first_half = ''.join(str(x) for x in range(1, i + 1))
        # Create the second half of the palindrome
        second_half = ''.join(str(x) for x in range(i - 1, 0, -1))
        # Print the full palindrome row
        print(first_half + second_half)

def show_help_message():
    print("Help:")
    print("A Palindromic Triangle is a triangular arrangement of numbers where each row forms a palindrome.")
    print("Example of a palindromic triangle:")
    print("1")
    print("11")
    print("121")
    print("12321")
    print("1234321")
    print("You can use this pattern to create a palindromic triangle for any number of lines.")

def main_menu():
    while True:
        print("\nMenu:")
        print("1- Display a right-angle triangle of ones")
        print("2- Display a palindromic triangle")
        print("3- Help")
        print("4- Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            lines = int(input("Enter the number of lines: "))
            display_right_angle_triangle(lines)
        elif choice == '2':
            lines = int(input("Enter the number of lines: "))
            display_palindromic_triangle(lines)
        elif choice == '3':
            show_help_message()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

main_menu()
