package zad4;

public class House extends Building {
    private int numberOfRooms;

    public House(String address, int yearOfConstruction, int numberOfRooms) {
        super(address, yearOfConstruction);
        this.numberOfRooms = numberOfRooms;
    }

    @Override
    public String toString() {
        return "Dom:\nadres: " + address +
                "\nrok budowy: " + yearOfConstruction +
                "\nliczba pokoi: " + numberOfRooms;
    }
}
