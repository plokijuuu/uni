import java.util.Arrays;
import java.util.Scanner;

public class zad6 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Podaj ilość elementów pierwszej tablicy: ");
        int size1 = scan.nextInt();
        System.out.println("Podaj liczby całkowite pierwszej tablicy: ");
        int[] num1 = new int[size1];
        for(int i = 0; i < size1; i++){
            num1[i] = scan.nextInt();
        }
        System.out.println("Podaj ilość elementów drugiej tablicy: ");
        int size2 = scan.nextInt();
        System.out.println("Podaj liczby całkowite drugiej tablicy: ");
        int[] num2 = new int[size2];
        for(int i = 0; i < size2; i++){
            num2[i] = scan.nextInt();
        }
        System.out.println("Pierwsza tablica posortowana bąbelkowo: "+ Arrays.toString(bubble_sort(num1,size1)));
        System.out.println("Druga tablica posortowana bąbelkowo: "+ Arrays.toString(bubble_sort(num2,size2)));

    }
    public static int[] bubble_sort(int[] tab, int size){
        for(int i = 0; i < size; i++){
            for(int j = 1; j < size - i; j++){
                if(tab[j - 1] > tab[j]){
                    int temp = tab[j - 1];
                    tab[j - 1] = tab[j];
                    tab[j] = temp;
                }
            }
        }
        return tab;
    }
}
