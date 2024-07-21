
def even_squares(numbers):
    
    squares = [x**2 for x in numbers if x % 2 == 0]
    return squares

def slice_list(numbers, start_index, end_index):
    # Slicing the list
    sublist = numbers[start_index:end_index]
    return sublist


def main():
    
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    
    even_square_list = even_squares(input_list)
    print("List of squares of even numbers:", even_square_list)
    
   
    start_index = 2
    end_index = 7
    sliced_list = slice_list(input_list, start_index, end_index)
    print(f"Sliced list from index {start_index} to {end_index}:", sliced_list)


if __name__ == "__main__":
    main()
