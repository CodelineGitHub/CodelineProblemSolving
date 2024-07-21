def display_right_angle_triangle(n):
    for i in range(1, n + 1):
        print('1 ' * i)
 
def display_palindromic_triangle(n):
    for i in range(1, n + 1):
        line = ' '.join(str(j) for j in range(1, i + 1))
        print(line + line[-2::-1])
 
def display_help():
    print("Help")
    print("A Palindromic Triangle is a triangular array of numbers where each row forms a palindrome.")
    print("The first few lines of a Palindromic Triangle are:")
    print("1\n11\n121\n12321\n1234321")
    print("You can use this pattern to draw a Palindromic Triangle for any number of lines.")


def main():
    while True:
        print("\nMenu:")
        print("1. Display a right-angle triangle of ones")
        print("2. Display a Palindromic Triangle")
        print("3. Help")
        print("4. Exit")
        choice = input("Enter your choice : ")
        if choice == '4':
            print("Exiting the program.")
            break
        elif choice == '3':
            display_help()
        elif choice in ('1', '2'):
            try:
                lines = int(input("Enter the number of lines : "))
                if lines > 0:
                    if choice == '1':
                        display_right_angle_triangle(lines)
                    elif choice == '2':
                        display_palindromic_triangle(lines)
            except ValueError:
                print("Invalid input. Please enter a number.")
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
 
if __name__ == "__main__":
    main()