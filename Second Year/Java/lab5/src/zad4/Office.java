package zad4;

public class Office extends Building{
    protected Integer numberOfCubicals;

    public Office(String address, Integer yearOfConstruction, Integer numberOfCubicals) {
        super(address, yearOfConstruction);
        this.numberOfCubicals = numberOfCubicals;
    }

    @Override
    public String toString() {
        return "Biuro:\nadres: " + address +
                "\nrok budowy: " + yearOfConstruction +
                "\nilość boksów: " + numberOfCubicals;
    }
}
