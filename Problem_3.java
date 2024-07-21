package codelineproblem3;

import java.util.Scanner;

public class CodelineProblem3 {

    public static void main(String[] args) {
        
        Scanner scanner = new Scanner(System.in);
        while (true) {
            displayMenu();
            System.out.print("Enter your choice: ");
            int choice = scanner.nextInt();
            
            switch (choice) {
                case 1:
                    displayOnesTriangle();
                    break;
                case 2:
                    displayPalindromicTriangle();
                    break;
                case 3:
                    displayHelp();
                    break;
                case 4:
                    System.out.println("Exiting the program.");
                    scanner.close();
                    return;
                default:
                    System.out.println("Invalid choice. Please enter a number from 1 to 4.");
            }
        }
        
    }
    
    public static void displayMenu() {
        System.out.println("Menu:");
        System.out.println("1. Display a right-angle triangle of ones");
        System.out.println("2. Display a palindromic triangle");
        System.out.println("3. Help");
        System.out.println("4. Exit");
    }

    public static void displayOnesTriangle() {
        System.out.println("Displaying a right-angle triangle of ones:");
        for (int i = 1; i <= 5; i++) {
            for (int j = 1; j <= i; j++) {
                System.out.print("1 ");
            }
            System.out.println();
        }
    }

    public static void displayPalindromicTriangle() {
        System.out.println("Displaying a palindromic triangle:");
        for (int i = 1; i <= 5; i++) {
            for (int j = 1; j <= i; j++) {
                System.out.print(j + " ");
            }
            for (int j = i - 1; j >= 1; j--) {
                System.out.print(j + " ");
            }
            System.out.println();
        }
    }

    public static void displayHelp() {
        System.out.println("Help");
        System.out.println("A Palindromic Triangle is a triangular array of numbers where each row forms a palindrome.");
        System.out.println("The first few lines of a Palindromic Triangle are:");
        System.out.println("1");
        System.out.println("11");
        System.out.println("121");
        System.out.println("12321");
        System.out.println("1234321");
        System.out.println("You can use this pattern to draw a Palindromic Triangle for any numbers of lines.");
    }
    
}
