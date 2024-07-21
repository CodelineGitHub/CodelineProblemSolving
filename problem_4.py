def squaresOfEvenNum(listInp):
    
    return [x ** 2 for x in listInp if x % 2 == 0]

def sliceSublist(lisInp, indexF, indexE):
   
    return lisInp[indexF:indexE]

def main():
    try:
       
        listInp = input("Enter the list of integers: ")

        
        if listInp.startswith('[') and listInp.endswith(']'):
            listInp = listInp[1:-1]  
            listInpS = [int(x.strip()) for x in listInp.split(',')]  
            
           
            squares = squaresOfEvenNum(listInpS)
            print("List of squares of even numbers:", squares)
            
            
            indexF = int(input("Enter start index: "))
            indexE = int(input("Enter end index: "))
            
            
            sublist = sliceSublist(listInpS, indexF, indexE)
            print("Sublist:", sublist)
        
        else:
            print("Invalid input format. Please enter the list in the format [1, 2, 3, 4].")
    
    except ValueError:
        print("Invalid input. Make sure the list contains integers separated by commas, and the indices are valid integers.")
    except IndexError:
        print("Index out of range. Make sure your indices are within the bounds of the list.")


main()

