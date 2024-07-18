def get_squares_of_even_numbers(input_list):
    # Create a new list of squares of even numbers using list comprehension
    even_squares = [x**2 for x in input_list if x % 2 == 0]
    return even_squares

def get_sublist(input_list, start_index, end_index):
    # Slice the original list to extract a sublist from start_index to end_index
    sublist = input_list[start_index:end_index]
    return sublist

def main():
    #List of Squares of Even Numbers:
    try:
        # Input a list of integers
        input_list = list(map(int, input("Enter a list of integers separated by spaces: ").split()))

        # Get the squares of even numbers
        even_squares = get_squares_of_even_numbers(input_list)
        print(f"Squares of even numbers: {even_squares}")

#Slice a Sublist from the List:
         # Input a list of integers
        input_list = list(map(int, input("Enter a list of integers separated by spaces: ").split()))


        # Input the start and end indices for slicing the list
        start_index = int(input("Enter the start index for slicing: "))
        end_index = int(input("Enter the end index for slicing: "))

        # Validate indices
        if start_index < 0 or end_index > len(input_list) or start_index > end_index:
            print("Invalid indices. Please enter valid start and end indices.")
        else:
            # Get the sublist
            sublist = get_sublist(input_list, start_index, end_index)
            print(f"Sublist from index {start_index} to {end_index}: {sublist}")

    except ValueError:
        print("Invalid input. Please enter valid integers.")

if __name__ == "__main__":
    main()