import java.util.Scanner;

public class InteractiveTriangleDisplay {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int choice;

        while (true) {
            displayMenu();
            choice = scanner.nextInt();
            scanner.nextLine();  // Consume newline

            switch (choice) {
                case 1:
                    System.out.print("Enter the number of lines: ");
                    int lines = scanner.nextInt();
                    displayRightAngleTriangle(lines);
                    break;
                case 2:
                    System.out.print("Enter the number of lines: ");
                    lines = scanner.nextInt();
                    displayPalindromicTriangle(lines);
                    break;
                case 3:
                    displayHelp();
                    break;
                case 4:
                    System.out.println("Exiting the program.");
                    scanner.close();
                    return;
                default:
                    System.out.println("Invalid choice. Please enter a number between 1 and 4.");
            }
        }
    }

    public static void displayMenu() {
        System.out.println("Menu:");
        System.out.println("1. Display a right-angle triangle of ones");
        System.out.println("2. Display a Palindromic Triangle");
        System.out.println("3. Help");
        System.out.println("4. Exit");
        System.out.print("Enter your choice: ");
    }

    public static void displayRightAngleTriangle(int lines) {
        for (int i = 1; i <= lines; i++) {
            for (int j = 1; j <= i; j++) {
                System.out.print("1");
            }
            System.out.println();
        }
    }

    public static void displayPalindromicTriangle(int lines) {
        for (int i = 1; i <= lines; i++) {
            for (int j = lines; j > i; j--) {
                System.out.print(" ");
            }
            for (int j = 1; j <= i; j++) {
                System.out.print(j);
            }
            for (int j = i - 1; j >= 1; j--) {
                System.out.print(j);
            }
            System.out.println();
        }
    }

    public static void displayHelp() {
        System.out.println("Help:");
        System.out.println("1. To display a right-angle triangle of ones, choose option 1 and enter the number of lines.");
        System.out.println("2. To display a Palindromic Triangle, choose option 2 and enter the number of lines.");
        System.out.println("3. To display this help message, choose option 3.");
        System.out.println("4. To exit the program, choose option 4.");
    }
}