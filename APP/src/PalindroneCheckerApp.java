public class PalindroneCheckerApp {

    public static void main(String[] args) {
        // Existing Use Case 1/2 code here

        // Call UC3 logic
        runUseCase3();
    }

    // Use Case 3 method
    public static void runUseCase3() {
        System.out.println("\n--- UC3: Palindrome Check Using String Reverse ---");

        String input = "racecar";
        String reversed = "";

        // Reverse string
        for (int i = input.length() - 1; i >= 0; i--) {
            reversed += input.charAt(i);
        }

        System.out.println("Original String: " + input);
        System.out.println("Reversed String: " + reversed);

        if (input.equals(reversed)) {
            System.out.println("Result: The string is a Palindrome.");
        } else {
            System.out.println("Result: The string is NOT a Palindrome.");
        }
    }
}
