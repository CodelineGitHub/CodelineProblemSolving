x = int(input ("Input:"))
i = []
while x > 0:
    remainder = x % 2 
    i.insert(0,str(remainder))
    x = x // 2
    z = "".join(i)
print ("Output:", z)