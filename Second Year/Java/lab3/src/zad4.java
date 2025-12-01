import java.util.Arrays;
import java.util.Scanner;

public class zad4 {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        System.out.println("Podaj liczbę elementów w tablicy: ");
        int size = scan.nextInt();
        System.out.println("Podaj liczby, które będą w tablicy: ");
        int[] ar = new int[size];
        for(int i = 0; i < size; i++){
            ar[i] = scan.nextInt();
        }
        int[] nar = new int[size];
        int new_size = 0;
        for(int i = 0; i < size; i++){
            if(!contain(ar[i],nar)){
                nar[new_size] = ar[i];
                new_size++;
            }
        }
        int[] bezpow = Arrays.copyOfRange(nar, 0,new_size);
        System.out.println("Wyświetlam nową tablicę bez powtórzeń: " + Arrays.toString(bezpow));

    }
    public static boolean contain(int a ,int[] b){
        for(int i : b){
            if(i == a){
                return true;
            }
        }
        return false;
    }
}
