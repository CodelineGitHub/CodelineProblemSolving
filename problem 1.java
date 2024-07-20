import java.util.Scanner;
import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class UserInputValidation {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Prompt for Username
        System.out.print("Enter Username: ");
        String username = scanner.nextLine();
        while (!isValidUsername(username)) {
            System.out.println("Invalid Username. It should not be empty and should not exceed 50 characters.");
            System.out.print("Enter Username: ");
            username = scanner.nextLine();
        }

        // Prompt for Password
        System.out.print("Enter Password: ");
        String password = scanner.nextLine();
        while (!isValidPassword(password)) {
            System.out.println("Invalid Password. It should be at least 8 characters long, contain at least one special symbol, one or more numbers, and one or more uppercase and lowercase characters.");
            System.out.print("Enter Password: ");
            password = scanner.nextLine();
        }

        // Prompt for Email
        System.out.print("Enter Email: ");
        String email = scanner.nextLine();
        while (!isValidEmail(email)) {
            System.out.println("Invalid Email. It should contain '@' symbol, alphanumeric characters before and after '@', and have letters with '.' character in between.");
            System.out.print("Enter Email: ");
            email = scanner.nextLine();
        }

        System.out.println("All inputs are valid.");
        scanner.close();
    }

    public static boolean isValidUsername(String username) {
        return username != null && !username.trim().isEmpty() && username.length() <= 50;
    }

    public static boolean isValidPassword(String password) {
        if (password.length() < 8) return false;
        boolean hasSpecialChar = false;
        boolean hasDigit = false;
        boolean hasUppercase = false;
        boolean hasLowercase = false;

        for (char c : password.toCharArray()) {
            if (Character.isDigit(c)) hasDigit = true;
            else if (Character.isUpperCase(c)) hasUppercase = true;
            else if (Character.isLowerCase(c)) hasLowercase = true;
            else hasSpecialChar = true;
        }

        return hasSpecialChar && hasDigit && hasUppercase && hasLowercase;
    }

    public static boolean isValidEmail(String email) {
        String emailRegex = "^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$";
        Pattern pattern = Pattern.compile(emailRegex);
        Matcher matcher = pattern.matcher(email);
        return matcher.matches();
    }
}
