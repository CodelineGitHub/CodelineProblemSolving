package codelineproblem4;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class CodelineProblem4 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Integer> numbers = new ArrayList<>(); 
        System.out.println("Enter the list of integers: ");
        int no = sc.nextInt();
        numbers.add(no);
       
        
        List<Integer> evenSquares = new ArrayList<>();
        for (Integer num : numbers) {
            if (num % 2 == 0) {
                evenSquares.add(num * num);
            }
        }
        System.out.println("List of squares of even numbers: " + evenSquares);
       
        System.out.println("Enter start index:");
        int start = sc.nextInt();
        System.out.println("Enter end index:");
        int end = sc.nextInt();
        System.out.println("Sublist:"+List<Integer>sliceList());
    }
    // Method to slice a list 
    public static List<Integer> sliceList(List<Integer> list, int startIndex, int endIndex) {
        if (startIndex < 0 || endIndex >= list.size() || startIndex > endIndex) {
            throw new IllegalArgumentException("Invalid start or end index");
        }
        return new ArrayList<>(list.subList(startIndex, endIndex + 1));
    }
    
}
