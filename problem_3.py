def print_triangle(n):
    for i in range(1, n + 1):
        print('*' * i)

def print_inverted_triangle(n):
    for i in range(n, 0, -1):
        print('*' * i)

def print_pyramid(n):
    for i in range(1, n + 1):
        print(' ' * (n - i) + '*' * (2 * i - 1))

def print_inverted_pyramid(n):
    for i in range(n, 0, -1):
        print(' ' * (n - i) + '*' * (2 * i - 1))

def main():
    while True:
        print("1. Print Triangle")
        print("2. Print Inverted Triangle")
        print("3. Print Pyramid")
        print("4. Print Inverted Pyramid")
        print("5. Exit")
        choice = int(input("Enter your choice (1-5): "))

        if choice == 1:
            n = int(input("Enter the number of rows: "))
            print_triangle(n)
        elif choice == 2:
            n = int(input("Enter the number of rows: "))
            print_inverted_triangle(n)
        elif choice == 3:
            n = int(input("Enter the number of rows: "))
            print_pyramid(n)
        elif choice == 4:
            n = int(input("Enter the number of rows: "))
            print_inverted_pyramid(n)
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
