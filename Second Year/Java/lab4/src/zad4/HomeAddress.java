package zad4;

public class HomeAddress {
    private Integer number;
    private String street;
    private String city;
    private String country;

    public HomeAddress(Integer number, String street, String city, String country) {
        this.number = number;
        this.street = street;
        this.city = city;
        this.country = country;
    }

    @Override
    public String toString() {
        return street + " " + number +
                ", " + city + ", " + country;

    }
}
