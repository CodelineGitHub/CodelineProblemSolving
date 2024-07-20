
def converDecimalToBinary(number):
    b = []
    # print('number = ',end=' ')
    while number>0:
        # print(number,end='')
        b.append (number%2)
        number = number//2
    b.reverse()
    print('Output: ',*b,sep='')
    # for i in b:
    #     print(i,sep='')
x = int( input('Input: '))
converDecimalToBinary(x)