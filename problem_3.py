#solving a problem of Interactive Triangle Display...
def print_menu():
    print("Menu:")
    print("1. Display a right-angle triangle of ones")
    print("2. Display a palindromic triangle")
    print("3. Help")
    print("4. Exit")

def right_angle_triangle():
    n = int(input("Enter the number of rows for the triangle: "))
    for i in range(1, n + 1):
        print("1 " * i)

def palindromic_triangle():
    n = int(input("Enter the number of rows for the triangle: "))
    for i in range(1, n + 1):
        row = " ".join(str(x) for x in range(1, i + 1))
        print(row + " " + row[::-1])

def display_help():
    print("This program allows you to:")
    print("- Display a right-angle triangle of ones")
    print("- Display a palindromic triangle")
    print("- Get help on how to use the program")
    print("- Exit the program")

#loop to choose the options ..
while True:
    print_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        right_angle_triangle()
    elif choice == '2':
        palindromic_triangle()
    elif choice == '3':
        display_help()
    elif choice == '4':
        print("Exit...")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
