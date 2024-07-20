A=[1,2,3,4,5,6,7,8,9,10]
print("The list is:")
print(A)
print("The squared of even numbers:")
squares_of_even = [x**2 for x in A if x % 2 == 0]
print(squares_of_even)
print("")
start_index = int(input("Enter a start index (within list range): "))
end_index = int(input("Enter an end index (within list range): "))
sublist = A[start_index:end_index]
print("")
print("sublist:")
print(sublist)