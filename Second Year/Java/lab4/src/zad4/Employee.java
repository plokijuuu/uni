package zad4;

public class Employee {
    private String name;
    private Double salary;
    private String hireDate;
    private HomeAddress homeAddress;

    public Employee(String name, Double salary, String hireDate, HomeAddress homeAddress) {
        this.name = name;
        this.salary = salary;
        this.hireDate = hireDate;
        this.homeAddress = homeAddress;
    }

    public String getInfo() {
        return "Imię: " + name +
                "\nData zatrudnienia: " + hireDate +
                "\nWynagrodzenie: " + String.format("%.2f", salary) +
                "\nAdres: " + homeAddress;
    }

    public void setNewAddress(HomeAddress newAddress) {
        this.homeAddress = newAddress;
    }

    public void raiseSalary(Double byPercent) {
        this.salary = this.salary * ((100 + byPercent) / 100 );
    }
}
