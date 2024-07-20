def get_even_squares(numbers):
    return [x ** 2 for x in numbers if x % 2 == 0]

def slice_list(numbers, start_index, end_index):
    return numbers[start_index:end_index]

def main():
    # Input a list of integers from the user
    numbers = list(map(int, input("Enter the list of integers: ").strip('[]').split(',')))

    # Generate the list of squares of even numbers
    even_squares = get_even_squares(numbers)
    print(f"List of squares of even numbers: {even_squares}")

    # Input start and end indices for slicing the list
    start_index = int(input("Enter the start index for slicing: "))
    end_index = int(input("Enter the end index for slicing: "))

    # Slice the list
    sliced_list = slice_list(numbers, start_index, end_index)
    print(f"Sliced list: {sliced_list}")

if __name__ == "__main__":
    main()
