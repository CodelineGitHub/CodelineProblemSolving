"""
@author: Shifa
Date: 20/7/2024
This program will convert psitive decimal to binary.

"""
#Enter input
print("Enter positive number: ", end=" ")
num = float(input())

#Check if input number is positive
if num >= 0 :
    
    #Convert dicemal to binary
    output=""
    while num > 0:
        output += str(int(num%2))
        num = num // 2
        
    #Reverse output
    output = output[::-1]
    
    #Display output
    print("Output: ", output)
else:
    print("The number is not positive")
    