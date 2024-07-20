"""
Author: Isra Musab Al Rasbi 
"""

'''
This function will conver from positive decimal number to its binary equivalent
Input: number
Output: binary
'''
def convert(n):
    #this is the base case
    #when n is 0 then return empty
    if n == 0:
        return ""
    #else, use recursion 
    else:
        #recursive call to update the number to be the quotient of the division
        binary = convert(n//2)
        
        #record the remainder
        return binary + str(n % 2)  

#ask the user to enter a number
number = int(input("Input: "))
#call the convert function 
output = convert(number)
#print the output
print(f"Output: {output}")
        