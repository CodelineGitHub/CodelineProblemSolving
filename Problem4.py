list_ = list(map(int,input("Enter the list of integers: ").strip('[]').split(',')))
newlist = []
for i in list_:
    if i % 2 == 0 : 
        newlist.append(i**2)
print("List of squares of even numbers: ",newlist)

start_index = int(input("Enter start index:"))
end_index = int(input("Enter end index:"))
sublist = list_[start_index:end_index]
print ("sublist: " , sublist)
