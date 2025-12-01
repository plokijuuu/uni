package zad4;

public class Main {
    public static void main(String[] args) {
        Building b1 = new Building("Warszawa, ul. Kwiatowa 5", 1990);
        House h1 = new House("Kraków, ul. Spacerowa 12", 2010, 5);
        Office o1 = new Office("Poznań, ul. Biznesowa 3", 2005, 30);
        Townhall t1 = new Townhall("Wrocław, Rynek 1", 1880, 120, "Jan Kowalski");

        System.out.println(b1);
        System.out.println(h1);
        System.out.println(o1);
        System.out.println(t1);
    }
}
