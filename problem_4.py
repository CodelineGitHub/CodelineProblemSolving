def even_squares_list(numbers):
    """Generate a list of squares for even numbers from the given list."""
    return [num * num for num in numbers if num % 2 == 0]

def extract_sublist(numbers, start, end):
    """Extract a sublist from the list based on the start and end indices."""
    return numbers[start:end]

def user_input_processing():
    """Process user input to generate even squares and extract a sublist."""
    # Input list of integers
    input_string = input("Please enter a list of integers (e.g., 1, 2, 3): ")
    int_list = list(map(int, input_string.split(',')))
    
    # Compute squares of even numbers
    even_squares = even_squares_list(int_list)
    print(f"Squares of even numbers: {even_squares}")

    # Get start and end indices for slicing
    start_idx = int(input("Enter the start index for slicing: "))
    end_idx = int(input("Enter the end index for slicing: "))
    
    # Extract and display sublist
    sublist = extract_sublist(int_list, start_idx, end_idx)
    print(f"Extracted sublist: {sublist}")

if __name__ == "__main__":
    user_input_processing()
