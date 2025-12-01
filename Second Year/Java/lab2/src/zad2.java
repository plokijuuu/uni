import java.util.Scanner;

public class zad2 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Wprowadź łańcuch znaków: ");
        String tekst = scan.nextLine();
        tekst = tekst.toLowerCase();
        tekst = tekst.replaceAll(" ", "");
        String spr = "aeiouyąę";
        System.out.println("Liczba poszczególnych samogłosek w podanym łańcuchu znakowym: ");
        for (int i=0; i<spr.length(); i++) {
            int licz = 0;
            for (int j=0; j<tekst.length(); j++) {
                if (spr.charAt(i) == tekst.charAt(j)) {
                    licz++;
                }
            }
            if(licz != 0) System.out.println(spr.charAt(i) + " : " + licz);

        }
    }
}
