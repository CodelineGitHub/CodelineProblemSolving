def get_even_squares(lst):
    return [x**2 for x in lst if x % 2 == 0]

def get_sublist(lst, start, end):
    return lst[start:end]

def main():
    # Get user input for the list of integers
    lst = list(map(int, input("Enter the list of integers (space-separated): ").split()))
    
    # Generate and display the list of squares of even numbers
    even_squares = get_even_squares(lst)
    print(f"List of squares of even numbers: {even_squares}")

    # Get user input for start and end indices for slicing the sublist
    start_index = int(input("Enter start index: "))
    end_index = int(input("Enter end index: "))
    sublist = get_sublist(lst, start_index, end_index)
    print(f"Sublist: {sublist}")

if __name__ == "__main__":
    main()
