from decimal import Decimal
Input = Decimal(input("Input: "))
def convert_num(Input):
    if Input == 0:
        return "0"
    binary = ""
    while Input>0:
    binary = str(Input % 2)+binary
        Input //=2
    return binary

print("Output:",convert_num(Input))
