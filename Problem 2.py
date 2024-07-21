def decimal_to_binary(n):
    
    if n <= 0:
        raise ValueError("Input must be a positive integer.")
    
    binary_representation = ""

    while n > 0:
        
        remainder = n % 2
        
        binary_representation = str(remainder) + binary_representation
       
        n = n // 2

    return binary_representation


inputs = [5, 255, 18]
for i in inputs:
    print(f"Input: {i}, Output: {decimal_to_binary(i)}")
