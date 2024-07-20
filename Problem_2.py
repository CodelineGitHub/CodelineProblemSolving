def decimal_to_binary(decimal_num):
    if decimal_num == 0:
        return '0'
    
    binary_num = ''
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary_num = str(remainder) + binary_num
        decimal_num //= 2
    
    return binary_num

# Example usage:
decimal_number = int(input("Enter a positive decimal number: "))
binary_number = decimal_to_binary(decimal_number)
print(f"The binary equivalent of {decimal_number} is: {binary_number}")

