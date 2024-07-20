List=[]
even=[]
range1=int(input("enter the range of your list: "))
for i in range(range1):
    num = int(input("Enter the list of integers: "))
    List.append(num)
    if num % 2 == 0:
        even.append(num**2)
print(List)
print("List of squares of even numbers: ",even)
start_index = int(input("Enter start index: "))
end_index = int(input("Enter end index: "))
print("sublist: ",List[start_index:end_index])
