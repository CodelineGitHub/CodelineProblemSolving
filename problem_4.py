import ast

def get_squares_of_even_numbers(numbers):
    """Create a new list of squares of even numbers using list comprehension."""
    return [x**2 for x in numbers if x % 2 == 0]

def get_sublist(numbers, start_index, end_index):
    """Slice the original list to extract a sublist from start_index to end_index."""
    return numbers[start_index:end_index]

def main():
    try:
        # Input list as a string
        raw_input = input("Enter a list of integers : ")
        
        # Convert the input string to a list using ast.literal_eval
        numbers = ast.literal_eval(raw_input)
        
        # Validate that the input is a list of integers
        if not isinstance(numbers, list) or not all(isinstance(x, int) for x in numbers):
            raise ValueError("The input must be a list of integers.")
        
        # Get squares of even numbers
        squares_of_even = get_squares_of_even_numbers(numbers)
        print("List of squares of even numbers:", squares_of_even)
    
        # Get slicing indices from the user
        start_index = int(input("Enter start index: ").strip())
        end_index = int(input("Enter end index: ").strip())
        
        # Extract sublist
        sublist = get_sublist(numbers, start_index, end_index)
        print("Sublist from index", start_index, "to", end_index, ":", sublist)
    
    except (ValueError, SyntaxError) as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()
