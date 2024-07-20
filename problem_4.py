#4

list_int = input("Enter list of integers: ")
list_int = list_int.strip('[]') #remove brackets
list_int = list_int.replace(',', ' ') #replace ',' with ''

listA = []
for part in list_int.split():
    listA.append(int(part))

# Task 1: Create a list of squares of even numbers
listB_square = []
for i in listA:
    if i % 2 == 0:
        listB_square.append(i**2)
print("List of squares of even numbers:", listB_square)

# Task 2: Slice a Sublist from the list
index1 = int(input("Enter start index: "))
index2 = int(input("Enter end index: "))

if (0 <= index1 < len(listA) and 0 <= index2 <= len(listA)):
    sublist = listA[index1:index2]
    print("Sublist:", sublist)
else:
    print("Invalid indices.")
