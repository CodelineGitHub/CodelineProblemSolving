def even_numbers(numbers):
    return [x**2 for x in numbers if x % 2 == 0]

def slice_list(numbers, start, end):
    return numbers[start:end+1]

def create():
    
    numbers = list(map(int, input("Enter a list of integers separated by spaces: ").split()))

    
    squares_of_even_numbers =even_numbers(numbers)
    print("List of squares of even numbers:",squares_of_even_numbers)

    
    start = int(input("Enter the start index for slicing: "))
    end = int(input("Enter the end index for slicing: "))

    
    sliced_list = slice_list(numbers, start, end)
    print("Sliced list:", sliced_list)

create()
