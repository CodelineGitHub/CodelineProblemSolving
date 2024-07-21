import java.util.Scanner;

public class UserLogin {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String username = "";
        String password = "";
        String email = "";
       
        while (true) {
            System.out.print("Username: ");
            username = scanner.nextLine().trim();

            if (username.length() > 50 || username.isEmpty() ) {
                System.out.println("Username is invalid");
            }
            else {
                System.out.println("Username is valid");
            }
       
       
        System.out.print("Password: ");
        password = scanner.nextLine().trim();
       
        if (password.length() > 50) {
                System.out.println("Password must be atleast 8 characters long, Please try again");
            }  
       
       String regex = "^(?=.*[a-zA-Z])(?=.*\\d)(?=.*[A-Z])(?=.*[a-z]).{8,}$";

        if (password.matches(regex)) {
            System.out.println("Password is valid.");
        } else {
            System.out.println("Password is invalid");
        }
       
        System.out.print("Email: ");
        email = scanner.nextLine().trim();
           
        String regex2 = "^[a-zA-Z0-9]+@[a-zA-Z0-9]+\\.[a-zA-Z]+$";

        if (email.matches(regex2)) {
            System.out.println("Email is valid.");
        } else {
            System.out.println("Email is invalid");
        }
break;
    }
           
       
    }
}
