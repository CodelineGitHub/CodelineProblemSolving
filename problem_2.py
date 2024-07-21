def convertToBinary(n):
    if n > 1:
        convertToBinary(n // 2)
    print(n % 2, end='')

# Input decimal number
dec = int(input("Input: "))


if dec == 0:
    print(0)
else:
    print("Output: ", end='')
    convertToBinary(dec)
    print()
    
# Keep the terminal window open
input("\nPress Enter to exit...")
