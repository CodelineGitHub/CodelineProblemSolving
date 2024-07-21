import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
       
        System.out.print("Enter a list of integers (add space between each integer): ");
        String inputLine = scanner.nextLine();
       
        System.out.print("Enter Start Index: ");
        int StartIndex = scanner.nextInt();
       
        System.out.print("Enter End Index: ");
        int EndIndex = scanner.nextInt();
       
        String[] tokens = inputLine.split("\\s+");
       
        List<Integer> integers = new ArrayList<>();
        for (String token : tokens) {
            try {
                int num = Integer.parseInt(token);
                integers.add(num);
            } catch (NumberFormatException e){
        }
        }
        System.out.println("List of integers entered:" + integers);
       
        List <Integer> EvenSquare = new ArrayList<>();
        for (int num : integers) {
       
        if (num % 2 == 0 ){
        int SquaredAns = num * num;
            EvenSquare.add(SquaredAns);
        }
        }
        System.out.println("List of Squares of Even Numbers: " + EvenSquare);
 
        List <Integer> IndexList = new ArrayList<>();
   
        for (int i = StartIndex; i <= EndIndex; i++) {
                IndexList.add(integers.get(i));
               
        }
        System.out.println("Sublist: " + IndexList);
       
       
        // Close the scanner
        scanner.close();
   

}
}
