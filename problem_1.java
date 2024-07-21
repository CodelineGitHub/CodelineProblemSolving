import java.util.Scanner;

public class CnvrtDToB {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        System.out.print("Input: ");
        int decNum = s.nextInt();
        s.close();

        String binNum = CnvrtDToB(decNum);
        System.out.println("Output: " + binNum);
    }

    public static String CnvrtDToB(int decNum) {
        StringBuilder binNum = new StringBuilder();

        while (decNum > 0) {
            int rmnd = decNum % 2;
            binNum.insert(0, rmnd);
            decNum = decNum / 2;
        }

        return binNum.toString();
    }
}

