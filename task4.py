def even_squares(lst):
    return [x**2 for x in lst if x % 2 == 0]

def slice_list(lst, start, end):
    return lst[start:end + 1]

numbers = input("Enter the list of int: ")
numbers = eval(numbers)
even_squares_list = even_squares(numbers)
print("List of 7 num:", even_squares_list)

start_idx = int(input("Enter start index: "))
end_idx = int(input("Enter end index: "))


sliced_list = slice_list(numbers, start_idx, end_idx)
print("Subilist:", sliced_list)
