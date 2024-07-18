def right_angle_triangle():
  """Displays a right-angle triangle of ones."""
  rows = int(input("Enter the number of lines: "))
  for i in range(1, rows + 1):
    print("1" * i)

def palindrome_triangle():
  """Displays a palindrome triangle."""
  rows = int(input("Enter the number of lines: "))
  for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    print("1" * (2 * i - 1))

def display_menu():
  """Displays the menu."""
  print("Menu:")
  print("1. Display a right-angle triangle of ones")
  print("2. Display a palindrome triangle")
  print("3. Help")
  print("4. Exit")

def main():
  """Runs the main loop of the program."""
  while True:
    display_menu()
    choice = int(input("Enter your choice: "))
    if choice == 1:
      right_angle_triangle()
    elif choice == 2:
      palindrome_triangle()
    elif choice == 3:
      print("Help:")
      print("A palindrome triangle is a triangular array of numbers where each row a palindrome.")
      print("the first few line of a palindrome triangle are:")
      print("1")
      print("11")
      print("121")
      print("12321")
      print("1234321")
      print("you can use this to drow a palindrome triangl for any number of line.")
    elif choice == 4:
        print("exiting the program")
        break
    else:
      print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
  main()