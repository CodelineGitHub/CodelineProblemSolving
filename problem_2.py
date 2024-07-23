def decimal_to_binary(decimal_number):
    if decimal_number == 0:
        return "0"

    binary_digits = []
    while decimal_number > 0:
        remainder = decimal_number % 2
        binary_digits.append(str(remainder))
        decimal_number = decimal_number // 2

    binary_digits.reverse()
    return ''.join(binary_digits)

def main():
    decimal_number = int(input("Enter a positive decimal number: "))
    if decimal_number < 0:
        print("Please enter a positive number.")
    else:
        binary_number = decimal_to_binary(decimal_number)
        print(f"Binary equivalent: {binary_number}")

if __name__ == "__main__":
    main()
