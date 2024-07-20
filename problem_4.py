# this library is imported to use the count function in the for loop
from itertools import count
numList = []
# this Menu is created to let the user choose which option the list should print
print("Menu:\n"
     "1. Create a list of squares of even numbers\n"
     "2. Create a sublist from a list\n")
m = input("Choose from the menu: ")
#----------------------------------------------------------------------------------------------
# the first program will take the values from the user to create a list
# then print a new list with squares of even numbers from the original list
if m == "1":
    for i in count():
        c = int(input("Enter your number: "))
        if not c % 2:
            num = c ** 2
            numList.append(num)
        a = input("Do you want to add more numbers? 'y' or 'n': ")
        if a == "y" or a == "Y":
            i += 1
        elif a == "n" or a == "N":
            print("List of squares of even numbers:", numList)
            break
        else:
            print("You have entered a wrong value.. ")
            break
#----------------------------------------------------------------------------------------------
# the second program will take the values for the list
# then create a sublist from the original list
# the user can choose in which index can start and end
elif m == "2":
    for i in count():
        c = int(input("Enter your number: "))
        numList.append(c)
        a = input("Do you want to add more numbers? 'y' or 'n': ")
        if a == "y" or a == "Y":
            i += 1
        elif a == "n" or a == "N":
            s = int(input("Enter Start index: "))
            e = int(input("Enter End index: "))
            print("Original list:", numList)
            sublist = numList[s:e]
            print("Sublist:", sublist)
            break
        else:
            print("You have entered a wrong value.. ")
            break
