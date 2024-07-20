def generate_even_squares(numbers):
    return [x**2 for x in numbers if x % 2 == 0]


def slice_sublist(numbers, start, end):
    return numbers[start:end]


def main():
    numbers = list(
        map(int, input("Enter the list of integers (comma-separated): ").split(',')))

    even_squares = generate_even_squares(numbers)
    print("List of squares of even numbers:", even_squares)

    start_index = int(input("Enter start index: "))
    end_index = int(input("Enter end index: "))
    sublist = slice_sublist(numbers, start_index, end_index)
    print("Sublist:", sublist)


if __name__ == "__main__":
    main()