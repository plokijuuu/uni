package zad3;

public class Tricycle extends Vehicle2{
    public Tricycle(String name, Integer numOfWheels, Difficulty difficulty) {
        super(name, numOfWheels, difficulty);
    }

    @Override
    public String toString() {
        return "Tricycle: " + getName() + " ilość kół: " + getNumOfWheels() +
                " trudność prowadzenia: " + getDifficulty() +
                " cena: " + getPrice();
    }

    @Override
    public boolean equals(Object obj) {
        if (!(obj instanceof Tricycle)) return false;
        Tricycle other = (Tricycle) obj;
        return this.getName().equals(other.getName());
    }
}
