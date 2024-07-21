#Problem 2: Convert Decimal to Binary
#Name: Juhaina Ahmed Al Siyabi
#Email: juhainaahmed123@icloud.com

def DecToBinary(): # Main Program
    # Prompt the user to enter a decimal number as an integer (e.g 12345 etc...)
    x = int(input("Input: "))

    DecToBin(x) #Once user inputs desired Decimal program calls the 'DecToBin' Function

def DecToBin(x):

    UserInput = [] #User Input stored

    # While loop to convert decimal to binary
    while x > 0:
        # Storing reminder in binary list
        UserInput.append(x % 2) 
        x = x // 2 

    # Printing binary numbers in reverse order
    print("Output: ", end="")
    for BinNum in reversed(UserInput):
        print(BinNum, end="")

if __name__ == "__main__":
    DecToBinary()
