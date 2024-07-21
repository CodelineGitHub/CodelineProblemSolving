```
# Function to convert decimal to binary
def decimal_to_binary(decimal):
if decimal == 0:
return "0"

binary = ""
while decimal > 0:
remainder = decimal % 2
binary = str(remainder) + binary
decimal = decimal // 2

return binary

# Input a positive decimal number
decimal_number = int(input("Enter a positive decimal number: "))

# Convert decimal to binary
binary_number = decimal_to_binary(decimal_number)

print("Binary equivalent:", binary_number)
```
