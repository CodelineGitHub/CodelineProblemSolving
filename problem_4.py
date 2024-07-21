
def process_list(numbers, start_index, end_index):
    # Create a new list of squares of even numbers from the original list
    even_squares = [x**2 for x in numbers if x % 2 == 0]
    
    # extract a sublist from start_index to end_index
    sublist = numbers[start_index:end_index]
    
    return even_squares, sublist

def list_of_integers():
    n = input("Enter a list of integers in the format [1, 2, 3, ...]: ")
    try:
        # Strip the square brackets and split by comma, then convert to integers
        numbers = [int(x.strip()) for x in n.strip('[]').split(',')]
        return numbers
    except ValueError:
        print("\nInvalid input format.\n Please enter a list of integers in the format [1, 2, 3, ...]")
        return list_of_integers()

original_list = list_of_integers()
start_index = int(input("Enter the start index: "))
end_index = int(input("Enter the end index: "))

even_squares, sublist = process_list(original_list, start_index, end_index)

# Output the results
print(f"Squares of even numbers: {even_squares}")
print(f"Sublist from index {start_index} to {end_index}: {sublist}")

# Keep the terminal window open 
input("\nPress Enter to exit...")