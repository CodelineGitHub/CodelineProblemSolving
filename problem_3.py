def display_menu():
    print("Menu:")
    print("1. Display a right-angle triangle of ones")
    print("2. Display a Palindromic Triangle")
    print("3. Help")
    print("4. Exit")

def right_angle_triangle(lines):
    for i in range(1, lines + 1):
        print('1' * i)

def palindromic_triangle(lines):
    for i in range(1, lines + 1):
        num = ''.join(str(x) for x in range(1, i + 1))
        print(num + num[-2::-1])

def display_help():
    print("Help:")
    print("A Palindromic Triangle is a triangular array of numbers where each row forms a palindrome.")
    print("The first few lines of a Palindromic Triangle are:")
    print("1")
    print("11")
    print("121")
    print("12321")
    print("1234321")
    print("You can use this pattern to draw a Palindromic Triangle for any number of lines.")

def main():
    while True:
        display_menu()
        select = input("Enter your choice: ")
        if select == '1':
            lines = int(input("Enter the number of lines: "))
            right_angle_triangle(lines)
        elif select == '2':
            lines = int(input("Enter the number of lines: "))
            palindromic_triangle(lines)
        elif select == '3':
            display_help()
        elif select == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
