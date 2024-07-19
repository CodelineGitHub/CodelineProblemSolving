
def decimal_to_binary(decimal_num):
    if decimal_num == 0:
        return "0"

    binary = ""
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary = str(remainder) + binary
        decimal_num //= 2

    return binary

def main():
    decimal_num = int(input("input: "))
    
    if decimal_num < 0:
        print("Error: Please enter a positive decimal number.")
    else:
        binary = decimal_to_binary(decimal_num)
        print(f"output: {binary}")

if __name__ == "__main__":
    main()
