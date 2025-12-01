package zad2;

public class Vehicle {
    public enum Difficulty { EASY, MEDIUM, HARD };

    private String name;
    private Integer numOfWheels;
    private Difficulty difficulty;

    public Vehicle(String name, Integer numOfWheels, Difficulty difficulty) {
        this.name = name;
        this.numOfWheels = numOfWheels;
        this.difficulty = difficulty;
    }

    public Integer getPrice() {
        return this.numOfWheels * 1000;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Difficulty getDifficulty() {
        return difficulty;
    }

    public void setDifficulty(Difficulty difficulty) {
        this.difficulty = difficulty;
    }

    public Integer getNumOfWheels() {
        return numOfWheels;
    }

    public void setNumOfWheels(Integer numOfWheels) {
        this.numOfWheels = numOfWheels;
    }

    @Override
    public String toString() {
        return "Vehicle: " + name + " ilość kół: " + numOfWheels +
                " trudność prowadzenia: " + difficulty +
                " cena: " + getPrice();
    }
}
