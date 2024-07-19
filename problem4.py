def get_even_squares(numbers):
    """Returns a list of squares of even numbers from the input list."""
    return [x ** 2 for x in numbers if x % 2 == 0]

def get_sublist(numbers, start_index, end_index):
    """Returns a sublist from the original list using the given start and end indices."""
    return numbers[start_index:end_index]

def main():
    try:
        # Taking input from the user for the list of integers
        input_list = input("Enter a list of integers in the format [1, 2, 3, ...]: ")
        numbers = eval(input_list)

        if not isinstance(numbers, list):
            raise ValueError("Input must be a list of integers.")
        for num in numbers:
            if not isinstance(num, int):
                raise ValueError("All elements in the list must be integers.")

        # Generating the list of squares of even numbers
        even_squares = get_even_squares(numbers)
        print(f"List of squares of even numbers: {even_squares}")

        # Taking input for the start and end indices for slicing
        start_index = int(input("Enter the start index for slicing: "))
        end_index = int(input("Enter the end index for slicing: "))

        # Getting the sublist
        sublist = get_sublist(numbers, start_index, end_index)
        print(f"Sublist from index {start_index} to {end_index}: {sublist}")

    except ValueError as e:
        print(f"Invalid input: {e}")
    except SyntaxError:
        print("Invalid input format. Please enter a list of integers in the correct format.")

if __name__ == "__main__":
    main()
