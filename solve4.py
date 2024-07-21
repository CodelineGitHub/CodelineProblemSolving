def even_squares(lst):
    return [x**2 for x in lst if x % 2 == 0]

def slice_list(lst, start, end):
    return lst[start:end + 1]

numbers = input("Enter the list of integers: ")
numbers = eval(numbers)

squares = even_squares(numbers)
print("List of squares of even numbers:", squares)

start_idx = int(input("Enter start index: "))
end_idx = int(input("Enter end index: "))

sliced = slice_list(numbers, start_idx, end_idx)
print("Sublist:", sliced)
