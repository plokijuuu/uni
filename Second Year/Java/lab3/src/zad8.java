import java.util.Arrays;

public class zad8 {
    public static void main(String[] args) {
        int[][] matrix = {{1,2,3},{4,5,6}};
        int size1 = matrix.length;
        int size2 = matrix[0].length;
        int[][] trans = new int[size2][size1];
        for(int i = 0; i < size1; i++) {
            for(int j = 0; j < size2; j++) {
                trans[j][i] = matrix[i][j];
            }
        }
        System.out.println("Macierz transponowana: " + Arrays.deepToString(trans));
    }
}
