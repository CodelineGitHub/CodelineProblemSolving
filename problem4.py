def generate_even_squares(input_list):
    """Generates a list of squares of even numbers using list comprehension."""
    return [x ** 2 for x in input_list if x % 2 == 0]

def slice_list(input_list, start_index, end_index):
    """Slices the original list to extract a sublist from start_index to end_index."""
    return input_list[start_index:end_index]

def main():
    # Input from the user for the list of integers
    user_input = input("Enter a list of integers separated by spaces: ")
    input_list = list(map(int, user_input.split()))

    # Generating list of squares of even numbers
    even_squares = generate_even_squares(input_list)
    print("List of squares of even numbers:", even_squares)

    # Getting start and end indices from the user
    start_index = int(input("Enter the start index for slicing: "))
    end_index = int(input("Enter the end index for slicing: "))

    # Slicing the list
    sliced_list = slice_list(input_list, start_index, end_index)
    print(f"Sliced list from index {start_index} to {end_index}:", sliced_list)

if __name__ == "__main__":
    main()
