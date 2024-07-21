def decimal_binary(decimal_num):
    if decimal_num == 0:
        return '0'
    
    binary = ''
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary = str(remainder) + binary
        decimal_num = decimal_num // 2
    
    return binary
def main():
    try:
        decimal_num = int(input("Input: "))
        if decimal_num < 0:
            raise ValueError("Please enter a positive decimal number.")
        
        binary_num = decimal_to_binary(decimal_num)
        print(f"Output : {binary_num}")
    
    except ValueError as ve:
        print(f"Error: {ve}")

if __name__ == "__main__":
    main()
