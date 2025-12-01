import java.util.Scanner;

public class zad2 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Witaj w aplikacji kalkulator!");
        System.out.println("Podaj pierwszą liczbę: ");
        int l1 = scan.nextInt();
        System.out.println("Podaj drugą liczbę: ");
        int l2 = scan.nextInt();
        System.out.println("Podaj symbol operacji (+,-,*,/): ");
        char sym = scan.next().charAt(0);
        if (sym == '+') {
            int wyn = l1 + l2;
            System.out.println("Wynik operacji " + l1 + " " + sym + " " + l2 + " = " + wyn);
        }
        else if (sym == '-') {
            int wyn = l1 - l2;
            System.out.println("Wynik operacji " + l1 + " " + sym + " " + l2 + " = " + wyn);
        }
        else if (sym == '*') {
            int wyn = l1 * l2;
            System.out.println("Wynik operacji " + l1 + " " + sym + " " + l2 + " = " + wyn);
        }
        else if (sym == '/') {
            if(l2 == 0) {
                System.out.println("Nie dzielimy przez 0!");
            }
            else {
                int wyn = l1 / l2;
                System.out.println("Wynik operacji " + l1 + " " + sym + " " + l2 + " = " + wyn);
            }
        }
        else {
            System.out.println("Wprowadzono błędny sysmbol operacji!");
        }

    }
}
