def triangle_display():
    print("Menu:")
    print("1. Display a right-angle triangle of ones")
    print("2. Display a Palindromic Triangle")
    print("3. Help")
    print("4. Exit")
def main():
    while True:
        triangle_display()
        choice = input("Enter your choice:")
        
        if choice == '1':
            def ones_triangle(lines):
                for i in range (1,lines+1):
                    print("1 "*i)
            lines = int(input("Enter the number of lines:"))   
            ones_triangle(lines)
        elif choice == '2':
            def Palindromic_triangle(rows):
                for i in range(1 , rows+ 1):
                    for j in range (1, i + 1):
                        print(j, end='')
                    for n in range (i-1, 0, -1):
                        print(n, end='')
                    print()
            rows =int(input("Enter the number of lines:"))      
            Palindromic_triangle(rows)
        elif choice == '3':
            print("""
Help:
A Palindromic Triangle is a triangular array of numbers where each row forms a Palindrome.
The first few lines of a Palindromic Triangle are:
1
11 
121 
12321 
1234321 
You can use pattern to draw a Palindromic Triangle for any number of lines.""")
        
        elif choice =='4':
            print("Exiting the Program.")
        else:
            print("Invalid choice!! Please choice a number from 1 - 4!")
main()