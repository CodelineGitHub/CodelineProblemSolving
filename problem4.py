def square_even_numbers(numbers):
    return [x**2 for x in numbers if x % 2 == 0]

def slice_list(numbers, start_index, end_index):
    return numbers[start_index:end_index]

def main():
    user_input = input("Enter a list of integers (comma-separated): ")
    numbers = list(map(int, user_input.split(',')))

    while True:
        print("\nMenu:")
        print("1. Display squares of even numbers")
        print("2. Display a slice of the list")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            even_squares = square_even_numbers(numbers)
            print("Squares of even numbers:", even_squares)
        
        elif choice == '2':
            start_index = int(input("Enter the start index for slicing: "))
            end_index = int(input("Enter the end index for slicing: "))
            sliced_list = slice_list(numbers, start_index, end_index)
            print("Sliced list:", sliced_list)
        
        elif choice == '3':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()
