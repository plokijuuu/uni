

public class zad1 {
    public static void main(String[] args){
        int[] num = {2,4,5,6,7,1,2,5,5,5,2};
        int sum = 0;
        for (int j : num) {
            sum += j;
        }
        System.out.println("Suma liczb całkowitych w tablicy wynosi: " + sum);

    }
}
