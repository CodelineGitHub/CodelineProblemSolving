# creating a function for getting the binary value
def binary(n):
    # creating a variable to store the binary value in a string format
    b = ""
    # creating a while loop that when the value is more than 0 it will keep running
    while n > 0:
        # get the mod of the decimal value then and make it as a string
        # then add it to the 'b' variable created and save the new value in same 'b' variable
        b = str(n % 2) + b
        # then update the value of the decimal by 2 until it reaches 0
        n = n//2
        # at the end of the function return the 'b' variable which represent the binary string value
    return b
# creating a variable 'd' that stores the value entered by the user
d = int(input("Input: "))
# printing the value of the binary
# by calling the function with the value of decimal number entered by the user
print("Output: " + binary(d))