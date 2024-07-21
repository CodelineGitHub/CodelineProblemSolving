
def decimal_to_binary(decimal_num):
    if decimal_num == 0:
        return "0"
    
    binary_result = ""
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary_result = str(remainder) + binary_result
        decimal_num = decimal_num // 2
    
    return binary_result

def main():
    while True:
        try:
            # Prompt the user to enter a positive decimal number
            user_input = input("Input: ")
            decimal_num = int(user_input)  # Convert input to integer
            
            if decimal_num < 0:
                print("Invalid positive decimal number.")
            else:
                # Convert the decimal number to binary and display the result
                binary_result = decimal_to_binary(decimal_num)
                print(f"Output: {binary_result}")
                break
                
        except ValueError:
            print("Invalid input.")

if __name__ == "__main__":
    main()
