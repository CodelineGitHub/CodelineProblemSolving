# Function to convert a decimal number to binary
def decimal_to_binary(number):
    # Initialize to store the binary result
    binary = ""
    
    # Edge case for when the number is 0
    if number == 0:
        return "0"
    
    # Loop until the number becomes 0
    while number > 0:
        # Get the remainder when the number is divided by 2 (0 or 1)
        remainder = number % 2
        
        # Convert the remainder to a string and add it to the binary string
        binary = str(remainder) + binary
        
        # Update the number to be the quotient of the division by 2
        number = number // 2
    
    # Return the final binary string
    return binary

# Main block to run the program
if __name__ == "__main__":
    # Take user input for the decimal number
    decimal_number = int(input("Enter a positive decimal number: "))
    
    # Call the function and print the binary equivalent
    binary_result = decimal_to_binary(decimal_number)
    print(f"Binary equivalent of {decimal_number} is: {binary_result}")
