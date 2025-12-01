package zad3;

public class Motorcycle extends Vehicle2{
    public Motorcycle(String name, Integer numOfWheels, Difficulty difficulty) {
        super(name, numOfWheels, difficulty);
    }

    @Override
    public String toString() {
        return "Motorcycle: " + getName() + " ilość kół: " + getNumOfWheels() +
                " trudność prowadzenia: " + getDifficulty() +
                " cena: " + getPrice();
    }

    @Override
    public boolean equals(Object obj) {
        if (!(obj instanceof Motorcycle)) return false;
        Motorcycle other = (Motorcycle) obj;
        return this.getName().equals(other.getName());
    }
}
