#solving a problem of  Generating Even Squares...

def squareslist(input_list, start_index, end_index):
    #Create a new list of squares of even numbers...
    squares_of_evens = [x ** 2 for x in input_list if x % 2 == 0]

    #Slice the original list to extract a sublist...
    sublist = input_list[start_index:end_index + 1]

    return squares_of_evens, sublist

# Example usage:
if __name__ == "__main__":
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    start_index = 2
    end_index = 5
    squareslist, sublist = squareslist(input_list, start_index, end_index)

    print("Original List:", input_list)
    print("Squares of even numbers:", squareslist)
    print(f"Sublist from index {start_index} to {end_index}: {sublist}")

    