def display_right_angle_triangle(rows):
    for i in range(1, rows + 1):
        print('1 ' * i)


def display_palindromic_triangle(rows):
    for i in range(1, rows + 1):
        line = ' '.join(str(j) for j in range(1, i + 1))
        line += ' ' + ' '.join(str(j) for j in range(i - 1, 0, -1))
        print(line)


def display_help():
    print("Help:")
    print("A palindromic triangle is a triangle array of numbers where each row forms a palindrome.")
    print("The first few lines of a palindromic triangle are:")
    print("1")
    print("11")
    print("121")
    print("12321")
    print("1234321")
    print("You can use this pattern to draw a palindromic triangle for any number of lines.")
    print("")


def main():
    while True:
        print("menu:")
        print("1. display a right-angle triangle of ones")
        print("2. display a palindromic triangle")
        print("3. help")
        print("4. exit")
        print("")
        choice = input("Enter your choice: ")

        if choice == '1':
            lines = int(input("Enter the number of lines: "))
            display_right_angle_triangle(lines)
        elif choice == '2':
            lines = int(input("Enter the number of lines: "))
            display_palindromic_triangle(lines)
        elif choice == '3':
            display_help()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")
        print("")


if __name__ == "__main__":
    main()
