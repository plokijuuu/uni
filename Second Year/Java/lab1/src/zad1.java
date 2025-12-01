import java.time.LocalDate;
import java.time.temporal.ChronoUnit;
import java.util.Scanner;

public class zad1 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Wprowdź swoje imię: ");
        String name =  scan.nextLine();
        System.out.println("Podaj rok urodzenia: ");
        int year = scan.nextInt();
        System.out.println("Podaj miesiąć urodzenia: ");
        int month = scan.nextInt();

        LocalDate birthdate = LocalDate.of(year, month, 1);
        LocalDate now = LocalDate.now();

        long diff = ChronoUnit.DAYS.between(birthdate, now);

        System.out.println("Cześć " + name + "!");
        System.out.println("Od twoich urodzin mineło " + diff + "dni");
    }
}
