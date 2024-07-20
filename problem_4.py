def display_menu():
    print("\n1. Creates a new list of squares of even numbers from the original list using list comprehension.")
    print("2. Slices the original list to extract a sublist from a given start index to a given end index")
    print("q. Exit\n")


def squares_of_even_numbers(numbers):
  return [num**2 for num in numbers if num % 2 == 0]

def slice_list(numbers, start, end):
  return numbers[start:end]



while True:
  display_menu()
  num = input("\nEnter Choice: ")
  if num == 'q':
    break
  numbers = [int(x) for x in input("Enter the list of integers separated by space: ").split()]
  if num == '1':
    squares = squares_of_even_numbers(numbers)
    if squares:
      print("\nList of Squares of even numbers:", squares)
    else:
      print("\nNo even numbers found in the list.")
  elif num == '2':
    start = int(input("\nEnter the starting index: "))
    end = int(input("Enter the ending index: "))
    if start >= 0 and end > start and end <= len(numbers):
      sublist = slice_list(numbers, start, end)
      print("\nSublist:", sublist)
      break
    else:
      print("Invalid indices. Please enter valid start and end indices.")

