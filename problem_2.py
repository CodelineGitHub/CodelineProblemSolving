def decimal_to_binary(n):

 if n==0:
    return "0"

 while n>0:
   decimal_to_binary(n//2)
   print(n%2,end='')
   break
Num=int(input("Enter a positive number:"))
decimal_to_binary(Num)

