
package codelineproblem2;

import java.util.Scanner;

public class CodelineProblem2 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Input: ");
        int decimal = sc.nextInt();
        
        if (decimal < 0) {
            System.out.println("Invalid, please enter a positive decimal number.");
            return;
        }
        
        String binary = decimalToBinary(decimal);
        System.out.println("Output: " + binary);
        
        sc.close();
    }
    
    public static String decimalToBinary(int decimal) {
        if (decimal == 0) {
            return "0";
        }
        
        StringBuilder binary = new StringBuilder();
        while (decimal > 0) {
            int remainder = decimal % 2;
            binary.insert(0, remainder); 
            decimal = decimal / 2;
        }
        
        return binary.toString();
    }
}
    
    

