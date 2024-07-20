def get_even_squares(numbers):
    return [x**2 for x in numbers if x % 2 == 0]

def get_sublist(numbers, start, end):
    return numbers[start:end]

try:
    input_list = input("Enter the list of integers (comma-separated): ").strip()
    integers_list = list(map(int, input_list.split(',')))    
    start_index = int(input("Enter start index: "))
    end_index = int(input("Enter end index: "))
    even_squares = get_even_squares(integers_list)
    print(f"List of squares of even numbers: {even_squares}")
    sublist = get_sublist(integers_list, start_index, end_index)
    print(f"Extracted sublist: {sublist}")
except ValueError:
    print("Invalid input.")
