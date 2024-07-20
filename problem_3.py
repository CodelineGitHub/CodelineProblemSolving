while True:
    print("\nMenu:")
    print("1. Display a right-angle triangle of ones")
    print("2. Display a Palindromic Triangle")
    print("3. Help")
    print("4. Exit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        n = int(input("Enter the number of lines: "))
        for i in range(1, n+1):
            print('1' * i)
    elif choice == '2':
        n = int(input("Enter the number of lines: "))
        for i in range(1, n + 1):
            if i == 1:
                print("1")
            else:
                for j in range(1, i):
                    print(j, end='')
                if i == 2:
                    print(i - 1, end='')
                for j in range(i - 2, 0, -1):
                    print(j, end='')
                print()
    elif choice == '3':
        print("\nHelp:")
        print("A Palindromic Triangle is a triangular array of numbers where each row forms a palindrome.")
        print("The first few lines of a Palindromic Triangle are:")
        print("1")
        print("11")
        print("121")
        print("12321")
        print("1234321")
        print("You can use this pattern to draw a Palindromic Triangle for any number of lines.")

    elif choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")