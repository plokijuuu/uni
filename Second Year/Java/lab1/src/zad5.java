import java.util.Scanner;

public class zad5 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Wybierz liczbę: ");
        int a = scan.nextInt();
        int wyn = liczjed(a);
        System.out.println("Ilość 1-bitów w reprezentacji binarnej podanej liczby wynosi " + wyn);
    }
    public static int liczjed(int n) {
        int licz = 0;
        while (n > 0) {
            if (n % 2 == 1) {
                licz++;
            }
            n /= 2;
        }
        return licz;
    }
}
