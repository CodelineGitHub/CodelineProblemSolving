"""
Author: Isra Musab Al Rasbi 
"""
import sys
'''
This function will calculate the square of the even numbers in the list
Input: list
Output: the square of the even numbers in the list
'''
def square_even(arr):
    return [i**2 for i in arr if i % 2 == 0]
            
'''
This function slice the list from a specific index
Input: list, start, end
Output: new list
'''
def slice_list(arr,a,b):
    return arr[a:b]


while True:
    print()
    print("Menu:") 
    print("1. List of Squares of Even Numbers")
    print("2. Slice a Sublist from the List")
    print("3. Exit")
    
    #add error handling 
    try:
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            try:
                #the input should be like this: 1 2 3 4 5 6 7 8 9 10
                arr_input = input("Enter the list of integers: ")
                arr = [int(x) for x in arr_input.split()]
                print("List of squares of even numbers: ",square_even(arr))
            except ValueError:
                print("Error!! please enter a list of integers separated by spaces")
                
        elif choice == 2:
            try:
                arr_input = input("Enter the list of integers: ")
                arr = [int(x) for x in arr_input.split()]
                start = int(input("Enter start index: "))
                end = int(input("Enter end index: "))
                print("Sublist: ",slice_list(arr, start, end))
            except ValueError:
                print("Error!! Please enter valid integers for the list and indices.")
                
        elif choice == 3:
            print("Exiting the program")
            sys.exit()
            
        else:
            print("Invalid choice")
    
    except ValueError:
        print("Invalid input")