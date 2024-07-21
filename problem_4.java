import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class GES {
    public static List<Integer> getES(List<Integer> nmbrs) {
        List<Integer> evnSq = new ArrayList<>();
        for (int num : nmbrs) {
            if (num % 2 == 0) {
                evnSq.add(num * num);
            }
        }
        return evnSq;
    }

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        System.out.print("Enter the list of integers (space-separated): ");
        List<Integer> nmbrs = new ArrayList<>();
        for (String str : s.nextLine().split(" ")) {
            nmbrs.add(Integer.parseInt(str));
        }

        List<Integer> evnSq = getES(nmbrs);
        System.out.println("List of squares of even numbers: " + evnSq);

        System.out.print("Enter start index: ");
        int startIndex = s.nextInt();
        System.out.print("Enter end index: ");
        int endIndex = s.nextInt();

        List<Integer> sublist = nmbrs.subList(startIndex, endIndex);
        System.out.println("Sublist: " + sublist);
        s.close();
    }
}

