public class zad1 {
    public static void main(String[] args) {
        //Przekształcenie przez podmiane

        String tekst = "Java to wspaniały język";
        tekst = tekst.replaceAll("wspaniały", "najlepszy");
        System.out.println(tekst);

        //Przekształcenie z użyciem podłańcuchów

        String tekst2 = "Java to wspaniały język";
        int p = tekst2.indexOf("wspaniały");
        String nowytekst = tekst.substring(0,p) + "najlepszy" + tekst.substring(p + "wspaniały".length());
        System.out.println(nowytekst);



    }
}
