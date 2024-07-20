#3

while True:
    print("1. Display a right-angle of ones\n2. Display a Palindromic Triangle\n3. Help\n4. Exit")
    x = int(input("Enter your choice: "))

    if x == 1 or x == 2:
        y = int(input("Enter the number of lines: "))
        if x == 1:
            for i in range(1, y + 1):
                print('1' * i)
        elif x == 2:
            for i in range(1, y + 1):
                # Print increasing numbers
                for j in range(1, i + 1):
                    print(j, end='')
                # Print decreasing numbers
                for j in range(i - 1, 0, -1):
                    print(j, end='')
                # Move to the next line
                print()
    elif x == 3:
        print("Help:\nA Palindromic Triangle is a triangle array of numbers where each row forms a palindrome.\nThe first few lines of a Palindromic Triangle are:\n1\n11\n121\n12321\n1234321\nYou can use this pattern to draw a Palindromic Triangle for any number of lines")
    elif x == 4:
        print("Exiting the program.")
        break
    else:
        print('Invalid choice.')
