# Taking input as a list of integers
int_list = eval(input("Enter the list of integers: "))

# Operation 1: Create a new list of squares of even numbers
even_squares = [x ** 2 for x in int_list if x % 2 == 0]
print("List of squares of even numbers:", even_squares)

# Operation 2: Slice the original list to extract a sublist
start_index = int(input("Enter start index: "))
end_index = int(input("Enter end index: "))
sublist = int_list[start_index:end_index]
print("Sublist:", sublist)