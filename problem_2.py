def convert_to_binary(n):
    if n == 0:
        return "0"
    
    binary_result = ""
    
    while n > 0:
        remainder = n % 2
        binary_result = str(remainder) + binary_result
        n = n // 2
    
    return binary_result

# Get user input
decimal_number = int(input("Enter a positive decimal number: "))
binary_number = convert_to_binary(decimal_number)
print(f"The binary equivalent of {decimal_number} is {binary_number}.")
