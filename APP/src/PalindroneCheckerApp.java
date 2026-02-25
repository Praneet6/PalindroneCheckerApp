import java.util.*;

public class PalindromeCheckerUC6 {

    public static boolean isPalindrome(String input) {

        // Remove spaces and convert to lowercase
        input = input.replaceAll("\\s+", "").toLowerCase();

        Queue<Character> queue = new LinkedList<>();
        Stack<Character> stack = new Stack<>();

        // Step 1: Insert characters into Queue and Stack
        for (char ch : input.toCharArray()) {
            queue.add(ch);      // enqueue
            stack.push(ch);     // push
        }

        // Step 2: Compare dequeue and pop
        while (!queue.isEmpty()) {
            if (!queue.remove().equals(stack.pop())) {
                return false;
            }
        }

        return true;
    }

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter a string to check palindrome:");
        String input = scanner.nextLine();

        if (isPalindrome(input)) {
            System.out.println("The string is a Palindrome.");
        } else {
            System.out.println("The string is NOT a Palindrome.");
        }

        scanner.close();
    }
}