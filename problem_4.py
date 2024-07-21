#Problem 4: Generating Even Squares
#Name: Juhaina Ahmed Al Siyabi
#Email: juhainaahmed123@icloud.com

def SquareGen():
    #Acquire input from user
    input_list = input("Enter a list of integers separated by spaces: ").split()
    input_list = [int(x) for x in input_list]

    #Creating a new list referring to the old list using List Comprehension method
    even_squares = [x**2 for x in input_list if x % 2 == 0]
    print("List of squares of even numbers:", even_squares)

    #Input the start and end indices for slicing
    start_index = int(input("Enter start index: ")) #Start Slice num
    end_index = int(input("Enter end index: ")) #End Slice num

    # Slice the original list to extract the sublist
    sublist = input_list[start_index:end_index]
    print("Sublist:", sublist)

if __name__ == "__main__":
    SquareGen()
