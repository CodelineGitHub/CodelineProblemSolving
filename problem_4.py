def get_even_squares(numbers):
    return [x**2 for x in numbers if x % 2 == 0]

def get_sublist(numbers, start, end):
    return numbers[start:end]

def main():
    try:
        numbers = list(map(int, input("Enter a list of integers separated by spaces: ").split()))
        even_squares = get_even_squares(numbers)
        print(f"List of squares of even numbers: {even_squares}")

        start_index = int(input("Enter the start index for slicing: "))
        end_index = int(input("Enter the end index for slicing: "))
        sublist = get_sublist(numbers, start_index, end_index)
        print(f"Sublist from index {start_index} to {end_index}: {sublist}")

    except ValueError:
        print("Invalid input. Please enter integers only.")

if __name__ == "__main__":
    main()
