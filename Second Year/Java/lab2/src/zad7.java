public class zad7 {
    public static void main(String[] args) {
        String numer = " 856 -234-456 ";
        numer = numer.replaceAll(" ", "");
        numer = numer.replaceAll("-", "");
        int temp = 3;
        int start = 0;
        String nowynumer = "";
        while (temp <= numer.length()) {
            nowynumer = nowynumer + numer.substring(start, temp);
            nowynumer = nowynumer + " ";
            start += 3;
            temp += 3;
        }
        nowynumer = nowynumer.trim();
        System.out.println(nowynumer);

    }
}
