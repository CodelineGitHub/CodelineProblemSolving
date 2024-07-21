def decimal_to_bin(num):
    if num == 0:
        return "0"
    
    bin_result = ""
    while num > 0:
        bin_result = str(num % 2) + bin_result
        num //= 2
    
    return bin_result

dec_num = int(input("Enter a positive decimal number: "))
bin_num = decimal_to_bin(dec_num)

print("Binary equivalent:", bin_num)
