import java.util.Scanner;
import java.util.Stack;

public class zad9 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Wprowadź ciąg nawiasów: ");
        String s = scan.nextLine();
        StringBuilder spr = new StringBuilder();
        boolean poprawny = true;

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if (c == '(' || c == '[' || c == '{') {
                spr.append(c);
            }

            else if (c == ')' || c == ']' || c == '}') {
                if (spr.isEmpty()) {
                    poprawny = false;
                    break;
                }

                char last = spr.charAt(spr.length() - 1);

                if ((c == ')' && last == '(') || (c == ']' && last == '[') || (c == '}' && last == '{')) {
                    spr.deleteCharAt(spr.length() - 1);
                }
                else {
                    poprawny = false;
                    break;
                }
            }
        }

        if (poprawny && spr.length() == 0) {
            System.out.println("Nawiasy są poprawne");
        }
        else {
            System.out.println("Nawiasy nie są poprawne");
        }
    }
}
