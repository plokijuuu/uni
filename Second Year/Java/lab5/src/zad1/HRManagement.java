package zad1;

import java.util.Scanner;

public class HRManagement {
    private static final Employee[] employees = new Employee[6];

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("HR Management System");

        while (true) {
            System.out.println("\nWybierz opcję:");
            System.out.println("[a] - dodaj pracownika");
            System.out.println("[s] - wyświetl listę pracowników");
            System.out.println("[q] - wyjście");

            char choice = scanner.next().charAt(0);

            switch (choice) {
                case 'a':
                    addEmployee(scanner);
                    break;

                case 's':
                    showEmployees();
                    break;

                case 'q':
                    System.out.println("Koniec programu.");
                    return;

                default:
                    System.out.println("Nieprawidłowy wybór!");
            }
        }
    }
    public static void showEmployees() {
        if  (employees[0] == null) {
            System.out.println("Brak pracowników.");
            return;
        }

        for(Employee employee: employees) {
            if(employee != null) {
                System.out.println(employee.toString());
            }
        }
    }
    public static void addEmployee(Scanner scanner) {
        System.out.println("Wybierz typ umowy pracownika:");
        System.out.println("[1] - umowa o pracę");
        System.out.println("[2] - freelancer");

        int type = scanner.nextInt();

        System.out.print("Imię: ");
        String fn = scanner.next();

        System.out.print("Nazwisko: ");
        String ln = scanner.next();

        switch (type) {
            case 1:
                System.out.print("Podstawowa pensja: ");
                double salary = scanner.nextDouble();

                System.out.print("Bonus: ");
                double bonus = scanner.nextDouble();

                Employee emp = new ContractOfEmployment(fn, ln, salary, bonus);
                CountandAdd(emp);
                break;

            case 2:
                System.out.print("Stawka godzinowa: ");
                double rate = scanner.nextDouble();

                System.out.print("Liczba godzin: ");
                int hours = scanner.nextInt();

                Employee em = new Freelancer(fn, ln, rate, hours);
                CountandAdd(em);
                break;

            default:
                System.out.println("Nieprawidłowy typ umowy pracownika!");
                break;
        }
    }

    private static void CountandAdd(Employee emp) {
        for (int i = 0; i < employees.length; i++) {
            if (employees[i] == null) {
                employees[i] = emp;
                return;
            }
        }

        for (int i = 0; i < employees.length; i++) {
            if (employees[i] instanceof Freelancer) {
                employees[i] = emp;
                return;
            }
        }

        employees[0] = emp;

    }
}
