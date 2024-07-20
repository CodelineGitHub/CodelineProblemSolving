#2

num=int(input("Input: "))
rem=0
record=[]
binary=''

hold=num
while(hold>0):
    quo=hold/2
    x=hold%2
    if(x>0):
        rem=1
    else:
        rem=0
    record.append(rem)
    hold=int(quo)

record.reverse()
for i in record:
    binary+=str(i)
    
print('output: ',binary)
