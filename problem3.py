def right_angle_triangle_of_ones(lines):
    for i in range(1, lines + 1):
        print('1' * i)

def palindromic_triangle(lines):
    for i in range(1, lines + 1):
        print(''.join(str(x) for x in range(1, i + 1)) + ''.join(str(x) for x in range(i - 1, 0, -1)))

def help_message():
    print("Help:")
    print("A Palindromic Triangle is a triangular array of numbers where each row forms a palindrome.")
    print("The first few lines of a Palindromic Triangle are:")
    print("1")
    print("11")
    print("121")
    print("12321")
    print("1234321")
    print("You can use this pattern to draw a Palindromic Triangle for any number of lines.")

def generate_even_squares(numbers):
    even_squares = [x ** 2 for x in numbers if x % 2 == 0]
    print(f"List of squares of even numbers: {even_squares}")

def main():
    while True:
        print("\nMenu:")
        print("1. Display a right-angle triangle of ones")
        print("2. Display a Palindromic Triangle")
        print("3. Help")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            lines = int(input("Enter the number of lines: "))
            right_angle_triangle_of_ones(lines)
        elif choice == '2':
            lines = int(input("Enter the number of lines: "))
            palindromic_triangle(lines)
        elif choice == '3':
            help_message()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
