package zad1;

public class Freelancer extends Employee {
    private Double hourlyRate;
    private Integer workHours;

    public Freelancer(String firstName, String lastName, Double hourlyRate, Integer workHours) {
        super(firstName, lastName, 0.0);
        this.hourlyRate = hourlyRate;
        this.workHours = workHours;
    }

    @Override
    public double calculateSalary() {
        return hourlyRate * workHours;
    }
}
