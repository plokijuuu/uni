package zad1;

class ContractOfEmployment extends Employee {
    private Double bonus;

    public ContractOfEmployment(String firstName, String lastName, Double salary, Double bonus) {
        super(firstName, lastName, salary);
        this.bonus = bonus;
    }

    @Override
    public double calculateSalary() {
        return this.salary + this.bonus;
    }
}
