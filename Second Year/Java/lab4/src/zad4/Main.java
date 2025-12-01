package zad4;

public class Main {
    public static void main(String[] args) {
        Employee[] employees = new Employee[3];
        employees[0] = new Employee(
                "Ania",
                3000.0,
                "2019-09-23",
                new HomeAddress(54,"Krakowska","Kraków","Polska")
        );
        employees[1] = new Employee(
                "Igor",
                4560.0,
                "2020-09-23",
                new HomeAddress(64,"Warszawska","Kraków","Polska")
        );
        employees[2] = new Employee(
                "Gosia",
                6781.0,
                "2015-01-03",
                new HomeAddress(4,"Złota","Warszawa","Polska")
        );

        System.out.println("Lista pracownikow przed podwyżką:\n");

        for(Employee employee : employees) {
            System.out.println(employee.getInfo());
            System.out.print("\n");
        }

        for(Employee employee : employees) {
            employee.raiseSalary(10.0);
        }

        System.out.println("Lista pracowników po podwyżce:\n");

        for(Employee employee : employees) {
            System.out.println(employee.getInfo());
            System.out.print("\n");
        }


    }
}
