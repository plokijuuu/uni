package zad1;

public abstract class Employee {
    private String firstName;
    private String lastName;
    protected Double salary;
    public Employee(String firstName, String lastName, Double salary) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.salary = salary;
    }

    public abstract double calculateSalary();

    @Override
    public String toString() {
        return firstName + ' ' + lastName + ' ' + calculateSalary();
    }
}
