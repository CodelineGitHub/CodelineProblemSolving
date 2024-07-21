package codelineproblem1;

import java.util.Scanner;

public class CodelineProblem1 {
    private static String username;
    private static String password;
    private static String email;
    private static Scanner sc = new Scanner(System.in);
    


    public static void main(String[] args) {
    
        displayUserInfo(); 
    }
        
       
    private static void setUsername() {
        System.out.print("username: ");
        String inputUsername = sc.nextLine();
        
        
        if (isValidUsername(inputUsername)) {
            username = inputUsername;
            System.out.println("Username is valid");
        } else {
            System.out.println("Username is Invalid");
        }
    }

    private static boolean isValidUsername(String username) {
        return !username.isEmpty() && username.length() <= 50;
    }

    private static void setPassword() {
        System.out.print("Password: ");
        String inputPassword = sc.nextLine();
        
     
        if (isValidPassword(inputPassword)) {
            password = inputPassword;
            System.out.println("Password is valid");
        } else {
            System.out.println("Password is Invalid");
        }
    }

    private static boolean isValidPassword(String password) {
        
        String specialSymbols = "!@#$%^&*()-_=+\\|[{]};:'\",<.>/?";
        boolean hasUpperCase = false;
        boolean hasLowerCase = false;
        boolean hasDigit = false;
        boolean hasSpecialChar = false;
        
        if (password.length() < 8) {
            return false;
        }
        
        for (char ch : password.toCharArray()) {
            if (Character.isUpperCase(ch)) {
                hasUpperCase = true;
            } else if (Character.isLowerCase(ch)) {
                hasLowerCase = true;
            } else if (Character.isDigit(ch)) {
                hasDigit = true;
            } else if (specialSymbols.contains(String.valueOf(ch))) {
                hasSpecialChar = true;
            }
        }
        
        return hasUpperCase && hasLowerCase && hasDigit && hasSpecialChar;
    }

    private static void setEmail() {
        System.out.print("Email: ");
        String inputEmail = sc.nextLine();
        
        
        if (isValidEmail(inputEmail)) {
            email = inputEmail;
            System.out.println("Email is valid");
        } else {
            System.out.println("Email is Invalid");
        }
    }

    private static boolean isValidEmail(String email) {
        
        if (!email.contains("@")) {
            return false;
        }
        
        String[] parts = email.split("@");
        if (parts.length != 2) {
            return false;
        }
        
        String localPart = parts[0];
        String domainPart = parts[1];
        
        
        if (localPart.isEmpty()) {
            return false;
        }
        
        
        if (!domainPart.contains(".") || domainPart.startsWith(".") || domainPart.endsWith(".")) {
            return false;
        }
        
        return true;
    }
    private static void displayUserInfo() {
        System.out.println("Username: " + username);
        System.out.println("Password: " + password);
        System.out.println("Email: " + email);
    }
    }
    

