def GenerateEvenSquares(numbers):
    EvenSquares = [num ** 2 for num in numbers if num % 2 == 0]
    return EvenSquares

def SliceList(numbers, start, end):
    SubList = numbers[start:end]
    return SubList

def main():
    try:
        NumbersInput = input("Enter The List of integers: ")
        numbers = list(map(int, NumbersInput.split()))

        EvenSquares = GenerateEvenSquares(numbers)
        print(f"List Squares of Even Numbers: {EvenSquares}")

        start = int(input("Enter start index: "))
        end   = int(input("Enter end index: "))

        if start < 0 or end > len(numbers) or start > end:
            print("Invalid indices. Please enter valid start and end indices.")
            return

        sublist = SliceList(numbers, start, end)
        print(f"Sublist from index {start} to {end}: {sublist}")

    except ValueError:
        print("Invalid input. Please enter integers only.")

if __name__ == "__main__":
    main()
