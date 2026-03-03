import java.util.Scanner;

class PalindromeChecker {

    private char[] stack;
    private int top;

    // Constructor
    public PalindromeChecker(int size) {
        stack = new char[size];
        top = -1;
    }

    // Push operation
    private void push(char ch) {
        stack[++top] = ch;
    }

    // Pop operation
    private char pop() {
        return stack[top--];
    }

    // Public method to check palindrome
    public boolean checkPalindrome(String input) {

        // Convert to lowercase and remove spaces
        input = input.toLowerCase().replaceAll("\\s", "");

        int length = input.length();

        // Push all characters into stack
        for (int i = 0; i < length; i++) {
            push(input.charAt(i));
        }

        // Compare with original string
        for (int i = 0; i < length; i++) {
            if (input.charAt(i) != pop()) {
                return false;
            }
        }

        return true;
    }
}

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a string: ");
        String input = sc.nextLine();

        PalindromeChecker checker = new PalindromeChecker(input.length());

        if (checker.checkPalindrome(input)) {
            System.out.println("It is a Palindrome!");
        } else {
            System.out.println("It is NOT a Palindrome!");
        }

        sc.close();
    }
}