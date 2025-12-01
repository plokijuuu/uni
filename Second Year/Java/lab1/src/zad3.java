import java.util.Scanner;

public class zad3 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Podaj liczbę n: ");
        int n = scan.nextInt();
        if(n <= 0) System.out.println("Ta liczba nie jest potęgą dwójki.");
        else{
            while(n % 2 == 0)
            {
                n /= 2;

            }
            if (n == 1) System.out.println("Ta liczba jest potęgą dwójki.");
            else System.out.println("Ta liczba nie jest potęgą dwójki.");
        }
    }
}
