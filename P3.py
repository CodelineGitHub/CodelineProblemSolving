```
def display_ones_triangle(rows):
for i in range(1, rows + 1):
print("1 " * i)

def display_palindromic_triangle(rows):
for i in range(1, rows + 1):
print((str(11**i))[:i].replace('1', ' ').strip())

# Display the menu
print("Menu:")
print("1. Display a right-angle triangle of ones")
print("2. Display a Palindromic Triangle")
print("3. Help")
print("4. Exit")

# Get user input for choice
choice = input("Enter your choice (1-4): ")

# Process the user's choice
while choice != "4":
if choice == "1":
rows = int(input("Enter the number of rows for the right-angle triangle: "))
display_ones_triangle(rows)
elif choice == "2":
rows = int(input("Enter the number of rows for the palindromic triangle: "))
display_palindromic_triangle(rows)
elif choice == "3":
print("Option 1 displays a right-angle triangle of ones.")
print("Option 2 displays a Palindromic Triangle.")
else:
print("Invalid choice. Please enter a valid option.")

# Display the menu again and get user input for the next choice
print("\nMenu:")
print("1. Display a right-angle triangle of ones")
print("2. Display a Palindromic Triangle")
print("3. Help")
print("4. Exit")
choice = input("Enter your choice (1-4): ")

print("Exiting the program.")
```
