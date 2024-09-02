def decimal_to_binary(decimal_number):
    # If the number is 0, directly return '0'
    if decimal_number == 0:
        return "0"

    # Initialize an empty string to store the binary number
    binary_number = ""

    # Loop until the number becomes 0
    while decimal_number > 0:
        remainder = decimal_number % 2  # Step 1: Divide the number by 2 and get the remainder (0 or 1)
        binary_number = str(remainder) + binary_number  # Step 2: Record the remainder
        decimal_number = decimal_number // 2  # Step 3: Update the number to be the quotient of the division

    return binary_number  # Step 5: The binary equivalent is the sequence of remainders read from bottom to top

# Ask the user to input a positive decimal number
user_input = int(input("Enter a positive decimal number: "))

# Convert the user's input to binary and display the result
binary_result = decimal_to_binary(user_input)
print(f"The binary equivalent of {user_input} is {binary_result}")
