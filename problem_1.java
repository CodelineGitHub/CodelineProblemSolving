import java.util.Scanner;
import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class ValidationOfUserInput {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String username = "";

        // Login Username validation
        while (true) {
            System.out.print("Enter Username: ");
            username = scanner.nextLine();
            if (username.isEmpty()) {
                System.out.println("Username cannot be empty.");
            } else if (username.length() > 50) {
                System.out.println("Username must be 50 characters or fewer.");
            } else {
                System.out.println("Username is valid.");
                break;
            }
        }

        // Login Password validation

         String password = "";

        while (true) {
            System.out.print("Enter Password: ");
            password = scanner.nextLine();
            
            if (password.length() < 8) {
                System.out.println("Password must be at least 8 characters long.");

            } else if (!password.matches(".*[!@#$%^&*(),.?\"*[!@#(),.?\":{}|<>]$%^&*.*")) {
                System.out.println("Password must contain at least one special symbol.");

            } else if (!password.matches(".*\\d.*")) {
                System.out.println("Password should have at least one number.");

            } else if (!password.matches(".*[A-Z].*")) {
                System.out.println("Password should have at least one uppercase character.");

            } else if (!password.matches(".*[a-z].*")) {
                System.out.println("Password should have at least one lowercase character.");

            } else {
                System.out.println("Password is valid.");
                break;
            }
        }

        String email = "";

        // Login Email validation
        while (true) {
            System.out.print("Enter Email: ");
            email = scanner.nextLine();
            
            if (!email.contains("@")) {
                System.out.println("Email should contain '@' symbol.");
            } else {
                String[] parts = email.split("@");
                if (parts.length != 2 || !parts[0].matches("[a-zA-Z0-9._%+-]+") || !parts[1].matches("[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}")) {
                    System.out.println("Email is not valid.");
                } else {
                    System.out.println("Email is valid.");
                    break;
                }
            }
        }

        scanner.close();
    }
}