def get_squares_of_even_numbers(numbers):
    return [x**2 for x in numbers if x % 2 == 0]

def slice_list(numbers, start_index, end_index):
    return numbers[start_index:end_index]

def main():
    try:
        
        input_list = input("Enter a list of integers separated by spaces: ")
        numbers = list(map(int, input_list.strip("[]").split(',')))
        
        
        squares_of_even_numbers = get_squares_of_even_numbers(numbers)
        print("List of squares of even numbers:", squares_of_even_numbers)
        
        
        start_index = int(input("Enter the start index for slicing the list: "))
        end_index = int(input("Enter the end index for slicing the list: "))
        
        
        sublist = slice_list(numbers, start_index, end_index)
        print("Sliced sublist:", sublist)
    
    except ValueError:
        print("Invalid input. Please enter integers only in the correct format.")

if __name__ == "__main__":
    main()
