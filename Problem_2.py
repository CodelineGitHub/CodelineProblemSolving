import java.util.Scanner;

public class DecimalToBinary {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Input: ");
        int PositiveInteger = scanner.nextInt();
       
       
        StringBuilder BinaryFormat = new StringBuilder();
       
        while ( PositiveInteger > 0 ) {
            int Remainder = PositiveInteger % 2;
            BinaryFormat.append(Remainder);
            PositiveInteger = PositiveInteger / 2;
           
        }
       
        BinaryFormat.reverse();
       
        System.out.println();
       
        System.out.print("Binary Equivalent is" + " " + BinaryFormat);

        scanner.close();
    }
}
