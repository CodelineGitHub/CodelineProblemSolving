def decimal_to_binary(decimal_number):
    if decimal_number == 0:
        return "0"
    
    remainders = []
    while decimal_number > 0:
        remainders.append(str(decimal_number % 2))
        decimal_number = decimal_number // 2
    
    remainders.reverse()  # Reverse the list to get the correct binary representation
    return ''.join(remainders)

# Get input from the user
user_input = int(input("Enter a positive decimal number: "))
binary_output = decimal_to_binary(user_input)

print(f"Input: {user_input}, Output: {binary_output}")
