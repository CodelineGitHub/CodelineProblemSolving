def get_squares_of_even_numbers(numbers):
    
    squares_of_evens = [num ** 2 for num in numbers if num % 2 == 0]
    
    return squares_of_evens


def get_sublist(numbers, start, end):
    
    sublist = numbers[start:end]
    
    return sublist


def main():
    
    numbers = list(map(int, input("Enter a list of integers (separated by spaces): ").split()))
    
    squares_of_evens = get_squares_of_even_numbers(numbers)
    
    print("\nSquares of even numbers: ", squares_of_evens)

    start = int(input("\nEnter the start index for slicing: "))
    
    end = int(input("Enter the end index for slicing: "))
    
    sublist = get_sublist(numbers, start, end)
    
    print("Sublist: ", sublist)


if __name__ == "__main__":
    main()
