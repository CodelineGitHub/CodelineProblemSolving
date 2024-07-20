import java.util.Scanner;

public class InteractiveProgram {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int choice;

        do {
            
            System.out.println("Menu:");
            System.out.println("1. Display a right-angle triangle of ones");
            System.out.println("2. Display a Palindromic Triangle");
            System.out.println("3. Help");
            System.out.println("4. Exit");
            choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    
                    System.out.print("Enter the number of lines: ");
                    int lines = scanner.nextInt();
                    rightAngleTriangle(lines);
                    break;

                case 2:
                    
                    System.out.print("Enter the number of lines: ");
                    int rows = scanner.nextInt();
                    palindromicTriangle(rows);
                    break;

                case 3:
                    
                    displayHelp();
                    break;

                case 4:
                    
                    System.out.println("Exiting the program!");
                    break;

                default:
                    System.out.println("  Enter a number between 1 and 4.");
            }

        } 

        scanner.close();
    }

    // Display a right-angle triangle of ones
    public static void rightAngleTriangle(int lines) {
        for (int i = 1; i <= lines; i++) {
            for (int j = 1; j <= i; j++) {
                System.out.print("1 ");
            }
            System.out.println();
        }
    }

    //  Display a Palindromic Triangle
    public static void palindromicTriangle(int rows) {
        for (int i = 1; i <= rows; i++) {

            
            for (int j = i; j < rows; j++) {
                System.out.print("  ");
            }

            
            for (int j = 1; j <= i; j++) {
                System.out.print(j + " ");
            }

            
            for (int j = i - 1; j >= 1; j--) {
                System.out.print(j + " ");
            }
            System.out.println();
        }
    }

    
}










