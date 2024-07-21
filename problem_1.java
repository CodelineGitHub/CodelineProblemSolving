import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class ULV {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
            System.out.println("Username:");
            String usrnm = s.nextLine();
            System.out.println("Password:");
            String psswrd = s.nextLine();
            System.out.println("Email:");
            String eml = s.nextLine();

            boolean isValdU = isValdU(usrnm);
            boolean isValdP = isValdP(psswrd);
            boolean isValdE = isValdE(eml);

            if (!isValdU) {
                System.out.println("Username is invalid.");
            } else {
                System.out.println("Username is valid.");
            }
            if (!isValdP) {
                System.out.println("Password is invalid.");
            } else {
                System.out.println("Password is valid.");
            }
            if (!isValdE) {
                System.out.println("Email is invalid.");
            } else {
                System.out.println("Email is valid.");
            }


    }

    static boolean isValdU(String usrnm) {
        if (usrnm.isEmpty() || usrnm.length() > 50) {
            return false;
        }
        return true;
    }

    static boolean isValdP(String psswrd) {
        if (psswrd.length() < 8 || !psswrd.matches(".*[a-z].*") || !psswrd.matches(".*[A-Z].*") || !psswrd.matches(".*\\d.*") || !psswrd.matches(".*[!@#$%^&*()].*")) {
            return false;
        }
        return true;
    }

    static boolean isValdE(String eml) {
        String regex = "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$";
        Pattern p = Pattern.compile(regex);
        Matcher m = p.matcher(eml);
        return m.matches();
    }
}

