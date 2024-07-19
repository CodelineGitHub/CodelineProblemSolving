def decimal_to_binary(decimal_number):
    if decimal_number == 0:
        return "0"
    
    binary_number = []
    
    while decimal_number > 0:
        remainder = decimal_number % 2
        binary_number.append(str(remainder))
        decimal_number = decimal_number // 2
    
    
    binary_number.reverse()
    
  
    return ''.join(binary_number)

def main():
    try:
        decimal_number = int(input("Enter a positive decimal number: "))
        if decimal_number < 0:
            raise ValueError("The number must be positive.")
        
        binary_number = decimal_to_binary(decimal_number)
        print(f"The binary equivalent of {decimal_number} is: {binary_number}")
    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()
  
