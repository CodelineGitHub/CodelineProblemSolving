def main():

    input_s = input("Enter the list of integers: ")
    
    input_List = [int(x) for x in input_s.strip('[]').split(',')]
    
    even_Squares = [x**2 for x in input_List if x % 2 == 0]
    
    print("List of squares of even numbers:", even_Squares)

if __name__ == "__main__":
    main()
