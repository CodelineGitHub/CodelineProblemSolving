def main():
    # Input: List of integers
    original_list = list(map(int, input("Enter a list of integers separated by spaces: ").split()))
    
    # Create a new list of squares of even numbers from the original list using list comprehension
    squares_of_even = [x**2 for x in original_list if x % 2 == 0]
    print("Squares of even numbers:", squares_of_even)
    
    # Input: Start and end index for slicing
    start_index = int(input("Enter the start index for slicing: "))
    end_index = int(input("Enter the end index for slicing: "))
    
    # Slice the original list to extract a sublist
    sublist = original_list[start_index:end_index]
    print("Sublist from index {} to {}: {}".format(start_index, end_index, sublist))

if __name__ == "__main__":
    main()
