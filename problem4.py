def list_of_squares_of_even_numbers(int_list):
    # List comprehension to create a new list of squares of even numbers
    even_squares = [x**2 for x in int_list if x % 2 == 0]
    return even_squares

def slice_list(int_list, start, end):
    # Slicing the original list to extract a sublist from start index to end index
    sublist = int_list[start:end]
    return sublist

def main():
    # Taking list of integers as input
    int_list = list(map(int, input("Enter a list of integers separated by spaces: ").split()))
    
    # Generating list of squares of even numbers
    even_squares = list_of_squares_of_even_numbers(int_list)
    print(f"List of squares of even numbers: {even_squares}")
    
    # Taking start and end indices for slicing
    start = int(input("Enter the start index for slicing: "))
    end = int(input("Enter the end index for slicing: "))
    
    # Slicing the list
    sublist = slice_list(int_list, start, end)
    print(f"Sliced list from index {start} to {end}: {sublist}")

if __name__ == "__main__":
    main()
