```
# Function to generate a list of squares of even numbers
def generate_even_squares(input_list):
even_squares = [num**2 for num in input_list if num % 2 == 0]
return even_squares

# Function to slice a sublist from the original list
def slice_sublist(input_list, start_index, end_index):
sublist = input_list[start_index:end_index+1]
return sublist

# Get the list of integers from the user
input_list = input("Enter the list of integers: ")
input_list = eval(input_list) # Convert the input string to a list

# Generate the list of squares of even numbers
even_squares_list = generate_even_squares(input_list)
print("List of squares of even numbers:", even_squares_list)

# Get the start and end indices for slicing the sublist
start_index = int(input("Enter start index: "))
end_index = int(input("Enter end index: "))

# Slice the sublist from the original list
sublist = slice_sublist(input_list, start_index, end_index)
print("Sublist:", sublist)
```
