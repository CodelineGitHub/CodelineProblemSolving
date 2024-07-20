import java.util.Scanner;
import java.util.Stack;

public class DecimalToBinary {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Prompt for a positive decimal number
        System.out.print("Enter a positive decimal number: ");
        int decimal = scanner.nextInt();

        // Validate input
        while (decimal < 0) {
            System.out.println("Please enter a positive number.");
            System.out.print("Enter a positive decimal number: ");
            decimal = scanner.nextInt();
        }

        // Convert decimal to binary
        String binary = convertToBinary(decimal);

        // Display the result
        System.out.println("Binary equivalent: " + binary);

        scanner.close();
    }

    public static String convertToBinary(int decimal) {
        // Edge case for 0
        if (decimal == 0) {
            return "0";
        }

        Stack<Integer> stack = new Stack<>();

        // Algorithm to convert decimal to binary
        while (decimal > 0) {
            int remainder = decimal % 2;
            stack.push(remainder);
            decimal = decimal / 2;
        }

        // Construct binary string from stack
        StringBuilder binary = new StringBuilder();
        while (!stack.isEmpty()) {
            binary.append(stack.pop());
        }

        return binary.toString();
    }
}

