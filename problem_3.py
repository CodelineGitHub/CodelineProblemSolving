def right_angle_triangle(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print("1", end=" ")
        print()

def display_palindromic_triangle(rows):
    for i in range(1, rows + 1):
        for j in range(1, rows - i + 1):
            print(" ", end=" ")
        for k in range(i, 0, -1):
            print(k, end=" ")
        for l in range(2, i + 1):
            print(l, end=" ")
        print()

def display_help():
    print("Menu Options:")
    print("1. Display a right-angle triangle of ones")
    print("2. Display a Palindromic Triangle")
    print("3. Help")
    print("4. Exit")

def main():
    while True:
        print("\nMenu:")
        print("1. Display a right-angle triangle of ones")
        print("2. Display a Palindromic Triangle")
        print("3. Help")
        print("4. Exit")
        
        choice = input("Enter your choice : ")

        if choice == '1':
            rows = int(input("Enter the number of lines: "))
            display_right_angle_triangle(rows)
        elif choice == '2':
            rows = int(input("Enter the number of lines: "))
            display_palindromic_triangle(rows)
        elif choice == '3':
            display_help()
        elif choice == '4':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
