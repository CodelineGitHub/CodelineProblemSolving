def print_even_squares(lst):
    print("List of squares of even numbers:", [i ** 2 for i in lst if i % 2 == 0])


def print_slice(lst):
    start = input("Enter start index: ")
    # Validate start index
    while not start.isdigit() or int(start) < 0 or int(start) > len(lst):
        print("Invalid start index.")
        start = input("Enter start index: ")

    end = input("Enter end index: ")
    # Validate end index
    while not end.isdigit() or int(end) > len(lst) or int(end) <= int(start):
        print("Invalid end index.")
        end = input("Enter end index: ")

    print("Sublist:", lst[int(start):int(end)])


def main():
    str_lst = input("Enter the list of integers: ")

    try:
        lst = [int(i) for i in str_lst.strip("[]").split(",")]

        print_even_squares(lst)
        print_slice(lst)

    except:
        print("Invalid input.\nExiting program...")
        exit()


if __name__ == '__main__':
    main()
