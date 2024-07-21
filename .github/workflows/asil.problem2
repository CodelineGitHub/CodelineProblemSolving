def decimal_to_binary(decimal_number):
    if decimal_number == 0:
        return "0"
    binary_number = ""
    while decimal_number > 0:
        binary_number = str(decimal_number % 2) + binary_number
        decimal_number = decimal_number // 2
    return binary_number

def main():
    while True:
        try:
            decimal_number = int(input("Enter a positive decimal number: "))
            if decimal_number < 0:
                print("Please enter a positive number.")
                continue
            binary_number = decimal_to_binary(decimal_number)
            print(f"Binary equivalent: {binary_number}")
            break
        except ValueError:
            print("Invalid input. Please enter a valid positive decimal number.")

if __name__ == "__main__":
    main()
