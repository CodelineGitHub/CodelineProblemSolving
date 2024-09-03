def decimal_to_binary(decimal_number):
    if decimal_number == 0:
        return "0"
    binary_number = ""
    while decimal_number > 0:
        remainder = decimal_number % 2
        binary_number = str(remainder) + binary_number
        decimal_number = decimal_number // 2
    return binary_number

def main():
    decimal_number = int(input("Enter a positive decimal number: "))
    if decimal_number < 0:
        print("Please enter a positive decimal number.")
        return
    print("Binary equivalent:", decimal_to_binary(decimal_number))

if __name__ == "__main__":
    main()