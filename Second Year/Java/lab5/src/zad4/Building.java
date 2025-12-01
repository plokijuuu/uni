package zad4;

public class Building {
    protected String address;
    protected Integer yearOfConstruction;

    public Building(String address, Integer yearOfConstruction) {
        this.address = address;
        this.yearOfConstruction = yearOfConstruction;
    }

    public String getAddress() {
        return address;
    }

    public int getYearOfConstruction() {
        return yearOfConstruction;
    }

    @Override
    public String toString() {
        return "Budynek:\nadres: " + address + "\nrok budowy: " + yearOfConstruction;
    }
}
