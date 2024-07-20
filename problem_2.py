def decimal_to_binary(decimal_number):
    if decimal_number > 1:
        decimal_to_binary(decimal_number // 2)
    print(decimal_number % 2, end = '')
    
number = int(input())
decimal_to_binary(number)