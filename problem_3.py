while True:
    print("\nMenu:")
    print("1. Display a rigth-angle triangle of ones")
    print("2. Display a palindromic triangle")
    print("3. help")
    print("4. exit")
    choice = input("Enter your choice: ")
    if choice=="1":
        num = int(input("Enter the number of lines: "))
        for i in range(num):
            print("1 " * (i+1))
    elif choice=="2":
        num = int(input("Enter the number of lines: "))
        for i in range(num):
            print(" " * (num-i) + "1" + "11" * i)
    elif choice=="3":
        print("\nHelp:")
        print("A palindromic triangle is a triangle array of numbers where each row forms a palindrome.")
        print("the first few lines of a palindromic triangle are: ")
        for i in range(num):
        print(" " * (num-i) + "1" + "11" * i)
        print("you can use this pattern to draw a palindromic trianglefor any number of lines")
    elif choice=="4":
        print("Exiting the program")
        break
    else:
        print("this choice is not available, try again!")
