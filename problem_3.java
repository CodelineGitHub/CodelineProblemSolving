import java.util.Scanner;
public class ITD {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int option;
        do {
            System.out.println("Menu:");
            System.out.println("1. Display a right-angle triangle of ones");
            System.out.println("2. Display a Palindromic Triangle");
            System.out.println("3. Help");
            System.out.println("4. Exit");
            System.out.print("Enter your choice: ");
            option = s.nextInt();
            switch (option) { 
                case 1: displayRAT(s);
                break;
                case 2: displayPT(s);
                break;
                case 3: displayH();
                break;
                case 4: System.out.println("Exiting the program.");
                break;
                default: System.out.println("Invalid choice. Please enter a number between 1 and 4.");
                } }
                while (option != 4);
                s.close();
                }
                
                static void displayRAT(Scanner s) {
                    System.out.print("Enter the number of lines: ");
                    int lin = s.nextInt();
                    for (int v = 1; v <= lin; v++) {
                        for (int w = 1; w <= v; w++) {
                            System.out.print("1");
                            }
                            System.out.println();
                            } }
                             
                            static void displayPT(Scanner s) {
                                System.out.print("Enter the number of lines: ");
                                int lin = s.nextInt();
                                for (int v = 1; v <= lin; v++) {
                                    for (int w = 1; w <= v; w++) {
                                        System.out.print(w);
                                        } 
                                        for (int w = v - 1; w >= 1; w--) {
                                            System.out.print(w);
                                            } 
                                            System.out.println();
                                            } }
                                           
                                            static void displayH() {
                                                System.out.println("Help:");
                                                System.out.println("A Palindromic Triangle is a triangle array of numbers where each row forms a palindrome.");
                                                System.out.println("The first few lines of a Palindromic Triangle are:");
                                                System.out.println("1");
                                                System.out.println("121");
                                                System.out.println("12321");
                                                System.out.println("1234321");
                                                System.out.println("You can use this pattern to draw a Palindromic Triangle for any number of lines.");
                                                } }
