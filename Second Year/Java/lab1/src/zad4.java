import java.util.Scanner;

public class zad4 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Podaj liczbę num: ");
        int num = scan.nextInt();
        int licz = 0;
        while (num > 0) {
            if(num % 2 == 0)
            {
                num /= 2;
            }
            else num--;
            licz++;
        }
        System.out.println("Liczba kroków potrzebnych do zredukowania liczby num do zera wynosi " + licz);

    }
}
