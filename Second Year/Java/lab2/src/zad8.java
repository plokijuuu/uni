import java.util.Scanner;

public class zad8 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Wprowadź łańcuch s: ");
        String s = scan.nextLine();
        int wyn = 0;
        for(int i = 0; i < s.length(); i++){
            for(int j = i + 1; j < s.length(); j++){
                if(s.charAt(i) == s.charAt(j)){
                    int temp = j - i - 1;
                    if(temp > wyn) wyn = temp;
                }
            }
        }
        System.out.println("Najdluzszy podciag miedzy dwoma takimi samymi znakami wynosi: " + wyn);
    }
}
