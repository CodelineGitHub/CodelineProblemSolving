def generate_even_squares(input_list):
    # Step 1: Create a new list of squares of even numbers
    even_squares = [num ** 2 for num in input_list if num % 2 == 0]

    return even_squares


def slice_list(input_list, start_index, end_index):
    # Step 2: Slice the original list
    sliced_list = input_list[start_index:end_index]

    return sliced_list


def main():
    # Input list of integers from user
    input_list = input("Enter a list of integers separated by spaces: ")
    input_list = list(map(int, input_list.split()))

    # Generate even squares
    even_squares = generate_even_squares(input_list)
    print(" List of Even squares:", even_squares)

    # Input start and end indices from user
    start_index = int(input("Enter the start index for slicing: "))
    end_index = int(input("Enter the end index for slicing: "))
    sliced_list = slice_list(input_list, start_index, end_index)
    print(
        f"Sliced list from index {start_index} to {end_index}: {sliced_list}")


if __name__ == "__main__":
    main()
