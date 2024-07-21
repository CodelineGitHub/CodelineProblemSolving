def right_angled_triangle(n):
   
   for i in range(n):
     for j in range(i+ 1):
      print("1",end='') 
     print()
 
def palindromic_triangle(n):
    n=5
    for i in range(n):
        p=1
        for j in range(i+1):
            print(p,end='')
            p+=1
        print()
 

def display_menu():
    print("\nTriangle Display Menu:")
    print("1. Display Right-Angled Triangle")
    print("2. Display Isosceles Triangle")
    print("3. Display Equilateral Triangle")
    print("4. Exit")

def create_lines():
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
             n=int(input("Enter the number of lines: "))
             right_angled_triangle(n)
             
        elif choice == '2':
             n=int(input("Enter the number of lines: "))
             palindromic_triangle(n)
        elif choice == '3':
             print("Help:\na plindromic triangele is a tringular array of number you can use this pattern to drw",palindromic_triangle(n))
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


create_lines()


  
  
