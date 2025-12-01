import java.util.Scanner;

public class zad6 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Wprowadź tekst: ");
        String tekst = scan.nextLine();
        if(tekst.isEmpty()){
            System.out.println("Jest to palindrom");
        }
        else{
            tekst = tekst.toLowerCase();
            //System.out.println(tekst);
            int start = 0;
            int end = tekst.length() - 1;
            int temp = 0;
            while(start <= end){
                if(!Character.isLetterOrDigit(tekst.charAt(start))){
                    start++;
                }
                else if(!Character.isLetterOrDigit(tekst.charAt(end))){
                    end--;
                }
                else if(tekst.charAt(start) != tekst.charAt(end)){
                    temp = 7;
                    break;
                }
                else{
                    start++;
                    end--;
                }
            }
            if(temp == 7){
                System.out.println("Nie jest to palindrom");
            }
            else{
                System.out.println("Jest to palindrom");
            }
        }

    }
}
