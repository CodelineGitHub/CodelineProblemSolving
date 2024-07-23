def get_even_squares(numbers):
    return [x**2 for x in numbers if x % 2 == 0]

def get_sublist(numbers, start_index, end_index):
    return numbers[start_index:end_index]

def main():
    # Get list of integers from the user
    numbers = list(map(int, input("Enter the list of integers (comma-separated): ").split(',')))
    
    # Get the squares of even numbers
    even_squares = get_even_squares(numbers)
    print(f"List of squares of even numbers: {even_squares}")

    # Get start and end index for slicing the list
    start_index = int(input("Enter start index: "))
    end_index = int(input("Enter end index: "))
    
    # Get the sublist
    sublist = get_sublist(numbers, start_index, end_index)
    print(f"Sublist: {sublist}")

if __name__ == "__main__":
    main()
