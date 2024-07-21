def DecimalToBinary(x):
    if x == 0:
        return "0"
    
    binary = ""
    while x > 0:
        remainder = x % 2
        binary = str(remainder) + binary
        x = x // 2
    
    return binary

DecimalNumber = int(input("Please input a positive decimal number: "))
binary_equivalent = DecimalToBinary(DecimalNumber)
print(f"The binary representation of {DecimalNumber} is {binary_equivalent}")
