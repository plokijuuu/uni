package zad3;

public class Car extends Vehicle2 {
    public Car(String name, Integer numOfWheels, Difficulty difficulty) {
        super(name, numOfWheels, difficulty);
    }

    @Override
    public String toString() {
        return "Car: " + getName() + " ilość kół: " + getNumOfWheels() +
                " trudność prowadzenia: " + getDifficulty() +
                " cena: " + getPrice();
    }

    @Override
    public boolean equals(Object obj) {
        if (!(obj instanceof Car)) return false;
        Car other = (Car) obj;
        return this.getName().equals(other.getName());
    }
}
