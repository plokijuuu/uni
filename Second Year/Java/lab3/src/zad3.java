import java.util.Arrays;

public class zad3 {
    public static void main(String[] args){
        int[] num1 = {2,4,5,6,7,1,2,5,5,5,2};
        int[] num2 = {1,2,3};
        int size = num1.length + num2.length;
        int[] sum = new int[size];
        for(int i = 0; i < num1.length; i++){
            sum[i] = num1[i];
        }
        for(int i = 0; i < num2.length; i++){
            sum[i + num1.length] = num2[i];
        }
        System.out.println("Nowa tablica:" + Arrays.toString(sum));



    }
}
