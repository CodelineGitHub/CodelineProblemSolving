import java.util.Scanner;

public class InteractiveTriangle {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
       
       

        System.out.print("Menu: ");
        System.out.println();
        System.out.print("1. Display a right-angle triangle of ones");
        System.out.println();
        System.out.print("2. Display a palinromic triangle");
        System.out.println();
        System.out.print("3. Help");
        System.out.println();
        System.out.print("4. Exit");
        System.out.println();
        System.out.println();
        System.out.print("Enter Your Choice: ");
        int Choice = scanner.nextInt();
       
        if (Choice == 4){
            System.out.println("Exiting the Program");
        }
       
        else if (Choice == 3){
            System.out.println("A Palinromic Triangle is a triangular array of numbers where each row forms a palindrome.");
            System.out.println("The first few lines of a Palinromic Triangle are:");
            System.out.println();
            System.out.println("1");
            System.out.println("11");
            System.out.println("121");
            System.out.println("12321");
            System.out.println("1234321");
            System.out.println();
            System.out.println("You can use this pattern to draw a Plalindromic Triangle for any number of lines");
        }
       
        else if (Choice ==2 ){
            System.out.print("Enter the number of lines: ");
        int NoOfLinesA = scanner.nextInt();
       
        for (int i = 1; i <= NoOfLinesA; i++) {
            StringBuilder row = new StringBuilder();
           
            for (int j = 1; j <= i; j++) {
                row.append(j);
            }

            for (int j = i - 1; j >= 1; j--) {
                row.append(j);
            }

            System.out.println(row.toString());
        }
       
       
       
    }
   
    else{
        System.out.print("Enter the number of lines: ");
        int NoOfLinesB = scanner.nextInt();
       
        for (int y =1; y <= NoOfLinesB; y++){
            for(int c = 1; c <=y; c++){
                System.out.print("1");
            }
            System.out.println();
        }
        scanner.close();
    }
}
}
