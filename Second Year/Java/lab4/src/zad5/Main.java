package zad5;

public class Main {
    public static void main(String[] args) {
        Employee employee = new Employee(
                "Ania",
                "2019-09-23",
                new HomeAddress(54,"Krakowska","Kraków","Polska"));

        System.out.println("Pracownik z domyślnym wynagrodzeniem:");
        System.out.println(employee.getInfo());

    }
}

