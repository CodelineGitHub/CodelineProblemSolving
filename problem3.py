
def display_right_angle_triangle(lines):
    
    for i in range(1, lines + 1):
        
        print("1 " * i)


def display_palindromic_triangle(lines):
    
    for i in range(1, lines + 1):
        num_str = ''.join(str(j) for j in range(1, i + 1))
        print(num_str + num_str[-2::-1])


def show_help():
    print("Help Menu:\n")
    print("1. Display a right-angle triangle of ones: Enter the number of lines and a triangle of ones will be displayed.")
    print("2. Display a palindromic triangle: Enter the number of lines and a palindromic triangle will be displayed.")
    print("3. Help: Show this help menu.")
    print("4. Exit: Exit the program.")
    

def main_menu():
    
    while True:
        
        print("\nMenu:")
        print("1. Display a right-angle triangle of ones")
        print("2. Display a palindromic triangle")
        print("3. Help")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            
            lines = int(input("Enter the number of lines: "))
            display_right_angle_triangle(lines)
            
        elif choice == "2":
            
            lines = int(input("Enter the number of lines: "))
            display_palindromic_triangle(lines)
            
        elif choice == "3":
            show_help()
            
        elif choice == "4":
            print("Exiting the program.")
