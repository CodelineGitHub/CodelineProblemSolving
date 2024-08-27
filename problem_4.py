def generate_even_squares(numbers):
    """
    Generates a list of squares of even numbers from the input list.

    :param numbers: List of integers.
    :return: List of squares of even integers.
    """
    even_squares = [x ** 2 for x in numbers if x % 2 == 0]
    return even_squares


def slice_sublist(numbers, start_index, end_index):
    """
    Slices a sublist from the input list based on the given start and end indices.

    :param numbers: List of integers.
    :param start_index: Starting index for slicing.
    :param end_index: Ending index for slicing.
    :return: Sliced sublist.
    """
    # Handle cases where indices might be out of bounds
    start_index = max(0, start_index)
    end_index = min(len(numbers), end_index)
    return numbers[start_index:end_index]


def main():
    """
    Main function to execute the program.
    """
    # Take input from the user for the list of numbers
    raw_input = input("Enter the list of integers: ")

    # Remove square brackets and split by comma
    numbers = list(map(int, raw_input.strip('[]').split(',')))

    # Generate and display the list of squares of even numbers
    even_squares = generate_even_squares(numbers)
    print(f"List of squares of even numbers: {even_squares}")

    # Take start and end indices as separate inputs
    start_index = int(input("Enter start index: "))
    end_index = int(input("Enter end index: "))

    # Slice and display the sublist
    sublist = slice_sublist(numbers, start_index, end_index)
    print(f"Sublist: {sublist}")


if __name__ == "__main__":
    main()
