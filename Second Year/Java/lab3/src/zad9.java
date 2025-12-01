public class zad9 {
    public static void main(String[] args) {
        int[] prices = {7,1,5,3,6,4};
        System.out.println("Maksymalny zysk jaki można osiągnąć wynosi: " + maxProfit(prices));
    }
    public static int maxProfit(int[] prices){
        int maxi = 0;
        int buy = prices[0];
        int temp = 0;
        for (int i = 0 ; i < prices.length ; i++) {
            temp = prices[i] - buy;
            if(maxi < temp){
                maxi = temp;
            }
            if(prices[i] < buy)
            {
                buy = prices[i];
            }
        }
        return maxi;
    }
}
