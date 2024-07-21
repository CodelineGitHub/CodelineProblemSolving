def decimalBinary(decimalNnm):
   
    if decimalNnm <= 0:
        return "enter a positive integer"
    
    
    if decimalNnm == 0:
        return "0"
    
    
    binaryNum = ""
    
   
    while decimalNnm > 0:
        remainder = decimalNnm % 2  
        binaryNum = str(remainder) + binaryNum
        decimalNnm = decimalNnm // 2  
    
    return binaryNum

def main():
   
   
   decimalNnm = int(input("Input: "))
        
       
   binary = decimalBinary(decimalNnm)
        
        
   print("output:", binary)
   


main()

