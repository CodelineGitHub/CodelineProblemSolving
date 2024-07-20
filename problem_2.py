def dec_to_bin(decimal):
    if decimal == 0:
        return "0"

    binary_representation = ""
    while decimal != 0:
        binary_representation += str(decimal % 2)  # Concatenate the remainder to previous remainders.
        decimal = decimal // 2  		# Update the num to be the quotient.

    return binary_representation[::-1]  # Return the remainders in reverse order


def main():
    decimal = input("Input: ")

    # Check that the entered value is a valid positive integer before proceeding
    if not decimal.isdigit():
        print("Invalid value entered. \nExiting program...")
        exit()

    print("Output:", dec_to_bin(int(decimal)))


if __name__ == "__main__":
    main()
