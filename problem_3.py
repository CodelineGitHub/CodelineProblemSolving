
#Create a displaing menu
def menu():
   print("Menu:")
   print("1. Display a right-angle triangle of ones")
   print("2. Display a palindromic Triangle")
   print("3. Help")
   print("4. Exit")


def right_angle(n):
   # Loop through each row from 1 to n
   for i in range(1,n+1):
       # Explanation:
        # - (10**i) creates a number with a 1 followed by i zeros.
        # - Subtracting 1 from this number gives us a sequence of i nines (e.g., 999 for i=3).
        # - Dividing this sequence of nines by 9 gives us a sequence of i ones (e.g., 111 for i=3).
      print(((10**i) - 1)//9)


def palindromic(n):
   for i in range(1,n+1):
       # Explanation:
        # - Squaring this sequence of ones results in a palindromic number (e.g., 111^2 = 12321).
      print((((10**i) - 1)//9)**2)


def help():
   print("Help:\n") 
   print("A Palindromic Triangle is a triangular arry of numbers where each row forms a palindrome.")
   print("The first few lines of a Palindromic Triangle are:\n") 
   for i in range(1, 6):  # Example with 5 rows
        print((((10**i) - 1) // 9) ** 2) 
   print("You can use this pattern to draw a Palindromic Triangle for any number of lines.") 


def main():
    while True:
        menu()
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            n = int(input("Enter the number of lines: "))
            right_angle(n)
            # Keep the terminal window open 
            input("\nPress Enter to exit...")
            break

        elif choice == 2:
            n = int(input("Enter the number of lines: "))
            palindromic(n)
            # Keep the terminal window open 
            input("\nPress Enter to exit...")
            break

        elif choice == 3:
            help()
            # Keep the terminal window open 
            input("\nPress Enter to exit...")
            break

        elif choice == 4:
            print("Exiting the program.")
            break

        else:
            print("Invalid choice, please try again.")

main()