def to_binary(dec):
    if dec == 0:
        return "0"
    bin_val = ""
    while dec > 0:
        bin_val = str(dec % 2) + bin_val
        dec = dec // 2
    return bin_val

#  decimal to binary
decimal_number = int(input("Enter a positive decimal number: "))
binary_number = to_binary(decimal_number)
print("Binary equivalent:", binary_number)
