package zad4;

public final class Townhall extends Office{
    private String mayor;

    public Townhall(String address, Integer yearOfConstruction, Integer numberOfCubicals, String mayor) {
        super(address, yearOfConstruction, numberOfCubicals);
        this.mayor = mayor;
    }

    @Override
    public String toString() {
        return "Ratusz:\nadres: " + address +
                "\nrok budowy: " + yearOfConstruction +
                "\nliczba boksów urzędniczych: " + numberOfCubicals +
                "\nburmistrz: " + mayor;
    }
}
