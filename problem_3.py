
def main():
  """Displays the menu and validates user input."""
  while True:
    print("\nMenu:")
    print("1. Display the right angle trinagle of ones")
    print("2. Display the palindromic Triangle")
    print("3. Help")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
      Line =int(input("Enter the number of Lines: "))
      for i in range(Line):
        print("1" * (1 * i + 1))
    elif choice == "2":
     def generate_pyramid(n):
          for i in range(1, n + 1):
              increasing_part = ''.join(str(x) for x in range(1, i + 1))
              decreasing_part = ''.join(str(x) for x in range(i - 1, 0, -1))
              print(increasing_part + decreasing_part)
     n =int(input("Enter the number of Lines: "))
     generate_pyramid(n)
    elif choice == "3":
     print("Help:")
     print("palindromic Triangle is a tringular array of numbers where each rows forms a palindrome.")
     print("The first few lines of a palindromic Triangle are:")
     print("1\n11\n121\n12321\n1234321")
    elif choice == "4":
      print("Exiting the program...")
      break
    else:
      print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
  main()
