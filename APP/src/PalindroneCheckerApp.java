/**
 * PalindroneCheckerApp
 *
 * UC4: Character Array Based Palindrome Check
 * Goal: Check if a string is a palindrome using char array and two-pointer technique
 *
 * Author: Praneet Rathore
 * Version: 4.0
 */
public class PalindroneCheckerApp {

    // UC4 Method
    public static void runUseCase4() {
        System.out.println("--- UC4: Character Array Based Palindrome Check ---");

        // Hardcoded input string
        String input = "racecar";

        // Convert string to character array
        char[] chars = input.toCharArray();

        // Two-pointer approach
        int start = 0;
        int end = chars.length - 1;
        boolean isPalindrome = true;

        while (start < end) {
            if (chars[start] != chars[end]) {
                isPalindrome = false;
                break;
            }
            start++;
            end--;
        }

        // Display results
        System.out.println("Input String: " + input);
        if (isPalindrome) {
            System.out.println("Result: The string is a Palindrome.");
        } else {
            System.out.println("Result: The string is NOT a Palindrome.");
        }
    }

    // Main method
    public static void main(String[] args) {
        runUseCase4(); // Call UC4
    }
}
