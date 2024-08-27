# Function to generate a list of squares of even numbers
def even_squares(numbers):
    # get squares of even numbers
    squares = [num ** 2 for num in numbers if num % 2 == 0]
    return squares

# Function to extract a sublist from the original list
def extract_sublist(numbers, start, end):
    # Slicing the list from start index to  the end index
    sublist = numbers[start:end]
    return sublist


if __name__ == "__main__":
    # enter input as a list of integers
    input_list = list(map(int, input("Enter the list of integers: ").strip("[]").split(",")))
    
    # printing the list of squares of even numbers
    even_squares_list = even_squares(input_list)
    print("List of squares of even numbers:", even_squares_list)
    
    # enter the input for start and end indexes
    start_index = int(input("Enter start index: "))
    end_index = int(input("Enter end index: "))
    
    # print the sublist 
    sublist = extract_sublist(input_list, start_index, end_index)
    print("Sublist:", sublist)
