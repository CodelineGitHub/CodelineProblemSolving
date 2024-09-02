def main():
    # Step 1: Get input from the user
    input_list = input("Enter a list of integers separated by spaces: ").split()
    # Convert input strings to integers
    int_list = [int(x) for x in input_list]
    
    # Step 2: Create a new list of squares of even numbers
    even_squares = [x ** 2 for x in int_list if x % 2 == 0]
    print("Squares of even numbers:", even_squares)
    
    # Step 3: Get start and end indices for slicing
    try:
        start_index = int(input("Enter the start index for slicing: "))
        end_index = int(input("Enter the end index for slicing: "))
        
        # Slice the original list
        sublist = int_list[start_index:end_index]
        print("Sliced sublist:", sublist)
        
    except ValueError:
        print("Invalid input. Please enter valid indices.")
    except IndexError:
        print("Index out of range. Please enter indices within the list bounds.")

if __name__ == "__main__":
    main()