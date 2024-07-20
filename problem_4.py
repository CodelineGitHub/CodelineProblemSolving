def even_squares(lst):
    return [x ** 2 for x in lst if x % 2 == 0]

def slice_sublist(lst, start, end):
    return lst[start:end]

def main():
    lst = list(map(int, input("Enter a list of integers separated by space: ").split()))
    start = int(input("Enter start index for slicing: "))
    end = int(input("Enter end index for slicing: "))
    
    print(f"List of squares of even numbers: {even_squares(lst)}")
    print(f"Sliced sublist: {slice_sublist(lst, start, end)}")

if __name__ == "__main__":
    main()
