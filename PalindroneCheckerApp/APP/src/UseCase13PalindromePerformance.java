import java.util.*;

public class UseCase13PalindromePerformance {

    // Method 1: Reverse String
    public static boolean reverseMethod(String text) {
        String reversed = new StringBuilder(text).reverse().toString();
        return text.equals(reversed);
    }

    // Method 2: Stack
    public static boolean stackMethod(String text) {
        Stack<Character> stack = new Stack<>();

        for(char c : text.toCharArray()) {
            stack.push(c);
        }

        String reversed = "";
        while(!stack.isEmpty()) {
            reversed += stack.pop();
        }

        return text.equals(reversed);
    }

    // Method 3: Deque
    public static boolean dequeMethod(String text) {
        Deque<Character> deque = new ArrayDeque<>();

        for(char c : text.toCharArray()) {
            deque.addLast(c);
        }

        while(deque.size() > 1) {
            if(deque.removeFirst() != deque.removeLast()) {
                return false;
            }
        }

        return true;
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a string:");
        String input = sc.nextLine();

        // Reverse method timing
        long start1 = System.nanoTime();
        boolean result1 = reverseMethod(input);
        long end1 = System.nanoTime();

        // Stack method timing
        long start2 = System.nanoTime();
        boolean result2 = stackMethod(input);
        long end2 = System.nanoTime();

        // Deque method timing
        long start3 = System.nanoTime();
        boolean result3 = dequeMethod(input);
        long end3 = System.nanoTime();

        System.out.println("\nResults:");

        System.out.println("Reverse Method: " + result1 +
                " Time = " + (end1 - start1) + " ns");

        System.out.println("Stack Method: " + result2 +
                " Time = " + (end2 - start2) + " ns");

        System.out.println("Deque Method: " + result3 +
                " Time = " + (end3 - start3) + " ns");

        sc.close();
    }
}