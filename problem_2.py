# converts a positive decimal number to binary equivalent.

def convert(n):
    """
    Converts a positive decimal number to its binary equivalent.

    Args:
        n (int): The decimal number to be converted.

    Returns:
        int: The binary equivalent of the input decimal number.
    """
    bin = 0
    i = 1

    while n != 0:
        rem = n % 2
        n //= 2
        bin += rem * i
        i *= 10

    return bin

def main():
    n = int(input("Input: Enter a decimal number: "))
    bin = convert(n)
    print(f" Output: {n} in decimal = {bin} in binary")

if __name__ == "__main__":
    main()