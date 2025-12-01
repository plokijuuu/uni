import java.util.Scanner;

public class zad3 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        StringBuilder tekst = new StringBuilder();
        System.out.println("Wyprowadź słowa (aby zkończyć wpisz koniec): ");
        while(true){
            String slowo = scan.nextLine();
            if(slowo.equalsIgnoreCase("koniec")){
                break;
            }
            tekst.append(slowo).append(" ");
        }
        System.out.println(tekst);

    }
}
