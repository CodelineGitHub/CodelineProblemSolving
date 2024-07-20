import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class EvenSquares {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Input list of integers
        System.out.print("Enter the list of integers (comma-separated): ");
        String input = scanner.nextLine();
        String[] inputArray = input.split(",");
        List<Integer> numbers = new ArrayList<>();

        for (String s : inputArray) {
            numbers.add(Integer.parseInt(s.trim()));
        }

        // Generate list of squares of even numbers
        List<Integer> evenSquares = generateEvenSquares(numbers);

        // Output the list of squares of even numbers
        System.out.println("List of squares of even numbers: " + evenSquares);

        // Input for slicing the list
        System.out.print("Enter start index for slicing: ");
        int startIndex = scanner.nextInt();
        System.out.print("Enter end index for slicing: ");
        int endIndex = scanner.nextInt();

        // Slice the list
        List<Integer> slicedList = sliceList(evenSquares, startIndex, endIndex);

        // Output the sliced list
        System.out.println("Sliced list: " + slicedList);

        scanner.close();
    }

    private static List<Integer> generateEvenSquares(List<Integer> numbers) {
        List<Integer> evenSquares = new ArrayList<>();
        for (int number : numbers) {
            if (number % 2 == 0) {
                evenSquares.add(number * number);
            }
        }
        return evenSquares;
    }

    private static List<Integer> sliceList(List<Integer> list, int start, int end) {
        if (start < 0 || end > list.size() || start > end) {
            throw new IndexOutOfBoundsException("Invalid start or end index.");
        }
        return new ArrayList<>(list.subList(start, end));
    }
}
