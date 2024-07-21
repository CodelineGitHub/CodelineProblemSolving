def square_of_evens(nums):
    # Use list comprehension to create a new list of squares of even numbers
    squares_of_evens = [num ** 2 for num in nums if num % 2 == 0]
    return squares_of_evens

def slice_list(nums, start, end):
    # Slice the original list to extract sublist from start to end-1 index
    sliced_list = nums[start:end]
    return sliced_list

def main():
    try:
        # Input list of integers
        input_list = input("Enter the list of integers: ")
        
        # Convert input string to list of integers
        nums = eval(input_list) 
        
        # Step 1: List of squares of even numbers
        squares_of_evens = square_of_evens(nums)
        print("List of squares of even numbers:", squares_of_evens)
        
        # Step 2: Slicing the original list
        start_index = int(input("Enter  start index : "))
        end_index = int(input("Enter end index : "))
        
        sliced_list = slice_list(nums, start_index, end_index)
        print(f"Sublist: {sliced_list}")
    
    except (ValueError, SyntaxError) as e:
        print("Error:", e)
        print("Please enter a valid list format, e.g., [1, 2, 3]")

if __name__ == "__main__":
    main()



