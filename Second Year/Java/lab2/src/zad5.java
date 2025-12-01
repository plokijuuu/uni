import java.util.Scanner;

public class zad5 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Wprowadź tekst: ");
        String tekst = scan.nextLine();
        tekst = tekst.toLowerCase().replaceAll(" ","");
        StringBuilder sb  = new StringBuilder(tekst);
        String tekst2 = sb.reverse().toString();
        if(tekst.equals(tekst2)){
            System.out.println("Jest to palindrom");
        }
        else {
            System.out.println("Nie jest to palindrom");
        }
    }
}
