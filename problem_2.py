def decimal_to_binary(decimal_number):
    if decimal_number == 0:
        return "0"
    
    binary_digits = []
    
    while decimal_number > 0:
        remainder = decimal_number % 2
        binary_digits.append(str(remainder))
        decimal_number //= 2
    
    # The binary digits are collected in reverse order, so reverse the list
    binary_digits.reverse()
    
    return ''.join(binary_digits)

def main():
    while True:
        try:
            decimal_number = int(input("Enter a positive decimal number: "))
            if decimal_number < 0:
                raise ValueError("The number must be positive.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}")
    
    binary_equivalent = decimal_to_binary(decimal_number)
    print(f"The binary equivalent of {decimal_number} is {binary_equivalent}")

if __name__ == "__main__":
    main()
