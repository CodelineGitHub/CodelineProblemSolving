import java.util.Scanner;
import java.util.Stack;

public class ConvertToBinary {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Input Method
        System.out.print("Enter a positive decimal number: ");
        int decimalNum = scanner.nextInt();

        // Convert  decimal  to binary
        String binaryString = ConvertToBinary(decimalNum);
        System.out.println("Output: " + binaryString);

        scanner.close();
    }

    // Method to convert decimal to binary
    public static String ConvertToBinary(int number) {
        Stack<Integer> stack = new Stack<>();

        // Process to convert decimal to binary
        while (number > 0) {
            int part = number % 2; // Find the part 
            stack.push(part); // Push the part onto the stack
            number = number / 2; 
        }

        StringBuilder binaryString = new StringBuilder();

        while (!stack.isEmpty()) {
            binaryString.append(stack.pop()); // Add each element to the binary string
        }

        return binaryString.toString(); // Return the binary representation as a string
    }
}
