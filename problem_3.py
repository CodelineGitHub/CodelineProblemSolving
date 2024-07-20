def display_menu():
    print("\nMENU")
    print("1. Display a right-angle triangle of ones")
    print("2. Display a Palindromic Triangle")
    print("3. Help")
    print("4. Exit")


def display_right_angle_triangle(rows):
    for i in range(1, rows + 1):
        print("1" * i)

def display_palindromic_triangle(rows):
    for i in range(1, rows + 1):
        for x in range(1,i):
            print(x,end='')
        if(i<=2):
            print('1')
            continue

        m = i-2
        for x in range(m,0,-1):
            print(x,end='')
        print()
        

def handle_choice(choice):
    if choice == '1':
        rows = int(input("Enter the number of rows: "))
        display_right_angle_triangle(rows)
    elif choice == '2':
        rows = int(input("Enter the number of rows: "))
        display_palindromic_triangle(rows)
    elif choice == '3':
        print('Help:\nA Palindromic Triangle is a triangular array of numbers where each row forms a palindrome.\nThe first few lines of a Palindromic Triangle are:\n')        
        display_palindromic_triangle(5) 
        print(' \nYou can use the above pattern to draw a Palindromic Triangle for any number of lines')
    elif choice == '4':
        print("Exiting the program...")
        return False  # Indicate exit
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
    return True  # Indicate to continue displaying the menu


while True:
    display_menu()
    choice = input("Enter your choice (1-4): ")
    if not handle_choice(choice):
        break
