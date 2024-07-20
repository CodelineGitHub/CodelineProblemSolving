def decimal_to_binary(decimal_num):
    if decimal_num == 0:
        return "0"
    
    binary_digits = []
    
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary_digits.append(str(remainder))
        decimal_num = decimal_num // 2
    
    # Reverse the list to get the binary representation
    binary_digits.reverse()
    binary_string = ''.join(binary_digits)
    
    return binary_string

def main():
    while True:
        try:
            decimal_num = int(input("Enter a positive decimal number (0 to exit): "))
            if decimal_num < 0:
                print("Please enter a positive number.")
                continue
            elif decimal_num == 0:
                print("Exiting program.")
                break
            else:
                binary_num = decimal_to_binary(decimal_num)
                print(f"The binary equivalent of {decimal_num} is: {binary_num}")
        except ValueError:
            print("Invalid input. Please enter a valid positive decimal number.")

if __name__ == "__main__":
    main()
