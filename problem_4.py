def find_largest_element(lst):
    return max(lst)

if __name__ == "__main__":
    elements = input("Enter a list of numbers separated by spaces: ").split()
    elements = [int(element) for element in elements]
    print(f"The largest element in the list is {find_largest_element(elements)}.")
