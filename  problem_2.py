def decimal_to_binary(dec_num):
    if dec_num == 0:
        return "0"

    binary_num = ""

    while dec_num > 0:
        remainder = dec_num % 2
        binary_num = str(remainder) + binary_num
        dec_num = dec_num // 2

    return binary_num

user_Input = int(input("Input: "))
binary_Output = decimal_to_binary(user_Input)
print(f"Output: {binary_Output}")
