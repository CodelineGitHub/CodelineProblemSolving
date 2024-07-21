def get_even_squares(numbers):
    return [x**2 for x in numbers if x % 2 == 0]

def slice_list(numbers, start_index, end_index):
    return numbers[start_index:end_index]

def main():
    print("Enter a list of integers separated by spaces:")
    numbers = list(map(int, input().split()))
    
    even_squares = get_even_squares(numbers)
    print("List of squares of even numbers:", even_squares)
    
    print("Enter the start index for slicing:")
    start_index = int(input())
    
    print("Enter the end index for slicing:")
    end_index = int(input())
    
    sublist = slice_list(numbers, start_index, end_index)
    print("Sliced sublist:", sublist)

if __name__ == "__main__":
    main()
