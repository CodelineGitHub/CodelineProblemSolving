
def decimal_to_binary(n):
    if n == 0:
        return "0"
    binary_number = []
    while n > 0:
        remainder = n % 2
        binary_number.append(str(remainder))
        n = n // 2
    binary_number.reverse()  # Since we need to read the remainders from bottom to top
    return ''.join(binary_number)

def main():
    try:
        decimal_number = int(input("Enter a positive decimal number: "))
        if decimal_number < 0:
            print("Please enter a positive number.")
        else:
            binary_number = decimal_to_binary(decimal_number)
            print(f"Input: {decimal_number} ")
            print(f"Output: {binary_number}" )
    except ValueError:
        print("Invalid input. Please enter a valid positive decimal number.")

if __name__ == "__main__":
    main()

