"""
@author: Shifa
Date: 20/7/2024
This program will generating even squares list and sublist.

"""
#Create list from input integer
nums=input("Enter a list of integers (press space between each number): ")
listt = list(map(int, nums.split()))

#Enter start and end index
print("Enter the start index: ",end="")
start= int(input())
print("Enter the end index: ",end="")
end= int(input())

#Square even number of the list and display result
squares = [value ** 2 for value in listt if value%2 == 0]
print("1) List that contain sqares even numbers: ", end="")
print(squares)

#Slice the list and display result
slices = [value for value in listt[start:end]]
print("2) Sublist: " , end="")
print(slices)
