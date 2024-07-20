def squares_of_evens(numbers):
    # List comprehension to create a new list of squares of even numbers
    squares = [num ** 2 for num in numbers if num % 2 == 0]
    return squares

def slice_list(numbers, start, end):
    # Slice the original list to extract sublist from start index to end index
    if start < 0:
        start = 0
    if end > len(numbers):
        end = len(numbers)
    sublist = numbers[start:end]
    return sublist

def main():
    try:
        # Taking input list of integers
        numbers = list(map(int, input("Enter a list of integers separated by spaces: ").split()))
        
        # Display original list
        print(f"Original list: {numbers}")
        
        # Option 1: Squares of even numbers
        even_squares = squares_of_evens(numbers)
        print(f"Squares of even numbers: {even_squares}")
        
        # Option 2: Slice the list
        start = int(input("Enter the start index for slicing: "))
        end = int(input("Enter the end index for slicing: "))
        sliced_list = slice_list(numbers, start, end)
        print(f"Sliced list from index {start} to {end}: {sliced_list}")
        
    except ValueError:
        print("Invalid input. Please enter integers separated by spaces.")

if __name__ == "__main__":
    main()
