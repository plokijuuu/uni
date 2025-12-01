import java.util.Scanner;

public class zad4 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Podaj łańcuch znakowy:");
        String tekst = scan.nextLine();
        //z użyciem String
        String tekst2 = "";
        for(int i = tekst.length()-1; i >= 0; i--) {
            tekst2 = tekst2 + tekst.charAt(i);
        }
        System.out.println(tekst2);
        //z użyciem StringBuilder
        StringBuilder tekst3 = new StringBuilder(tekst);
        tekst3.reverse();
        System.out.println(tekst3);
    }
}
