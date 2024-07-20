def decimal_to_binary(decimal_number):
    if decimal_number == 0:
        return "0"

    binary_number = ""
    while decimal_number > 0:
        remainder = decimal_number % 2
        binary_number = str(remainder) + binary_number
        decimal_number = decimal_number // 2
    
    return binary_number

def main():
    # Input from the user
    decimal_number = int(input("Enter a positive decimal number: "))
    
    # Validate input
    if decimal_number < 0:
        print("Please enter a positive number.")
        return

    binary_number = decimal_to_binary(decimal_number)
    print(f"The binary equivalent of {decimal_number} is {binary_number}")

if __name__ == "__main__":
    main()
