num=int(input("Input: "))
if num <= 0:
    print("Input must be a positive decimal number")
binary_string = ""
while num > 0:
    remainder = num % 2 
    binary_string = str(remainder) + binary_string 
    num //= 2
print("Output: "+ binary_string)