
# solution problem two
def decimal_to_binary(decimal_num):
    if decimal_num == 0:
        return "0"
    
    binary_digits = []
    
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary_digits.append(str(remainder))
        decimal_num //= 2
    
    binary_digits.reverse()
    binary_str = "".join(binary_digits)
    return binary_str

def main():
    decimal_num = int(input("Enter a positive decimal number: "))
    
    if decimal_num < 0:
        print("Please enter a positive number.")
        return
    
    binary_str = decimal_to_binary(decimal_num)
    
    print(f"The binary equivalent of {decimal_num} is: {binary_str}")

if __name__ == "__main__":
    main()







