import java.util.Scanner;

public class zad2 {
    public static void main(String[] args){
        int[] num = {2,4,5,6,7,1,2,5,5,5,2};
        Scanner scan = new Scanner(System.in);
        System.out.println("Podaj liczbe x: ");
        int x = scan.nextInt();
        int licz = 0;
        for (int i : num)
        {
            if(x == i){
                licz++;
            }
        }
        System.out.println("Liczba " + x + " występuje w tablicy num " + licz + " razy");
    }
}
