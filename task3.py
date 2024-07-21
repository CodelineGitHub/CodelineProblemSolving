def ones_triangle(n):
    for i in range(1, n + 1):
        print("1 " * i)

def palindrome_triangle(n):
    for i in range(1, n + 1):
        print((str(11 ** i))[:i].replace('1', ' ').strip())

# Display the menu for chooses 
print("Menu:")
print("1. Display a right-angle triangle of ones")
print("2. Display a Palindromic Triangle")
print("3. Help")
print("4. Exit")


choice = input("Enter your choice (1-4): ")

while choice != "4":
    if choice == "1":
        rows = int(input("Enter the number of rows for the right-angle triangle: "))
        ones_triangle(rows)
    elif choice == "2":
        rows = int(input("Enter the number of rows for the palindromic triangle: "))
        palindrome_triangle(rows)
    elif choice == "3":
        print("Option 1 displays a right-angle triangle of ones.")
        print("Option 2 displays a Palindromic Triangle.")
    else:
        print("Invalid choice. Please enter a valid option.")

    print("\nMenu:")
    print("1. Display a right-angle triangle of ones")
    print("2. Display a Palindromic Triangle")
    print("3. Help")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

print("Exiting the program.")
