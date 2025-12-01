import java.util.Arrays;
import java.util.Scanner;

public class zad5 {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        int[] num = {2,2,3,8,1,0};
        System.out.println("Podaj indeks (0-5), na którym chcesz, żeby znajdował się nowy element: ");
        int id = scan.nextInt();
        System.out.println("Podaj element do wstawienia: ");
        int x = scan.nextInt();
        int[] nw_num = new int[num.length + 1];
        int temp = 0;
        for(int i = 0; i < num.length; i++){
            if(i == id){
                nw_num[i] = x;
                temp++;
            }
            else{
                nw_num[i] = num[i - temp];
            }
        }
        System.out.println("Nowa utworzona tablica z przesunięciem: " + Arrays.toString(nw_num));



    }

}
