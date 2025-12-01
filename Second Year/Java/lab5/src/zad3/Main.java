package zad3;

public class Main {
    public static void main(String[] args) {
        Vehicle2 car1 = new Car("Audi", 4, Vehicle2.Difficulty.MEDIUM);
        Vehicle2 car2 = new Car("Audi", 4, Vehicle2.Difficulty.MEDIUM);
        Vehicle2 moto = new Motorcycle("Honda", 2, Vehicle2.Difficulty.HARD);
        Vehicle2 trike = new Tricycle("Trike 3000", 3, Vehicle2.Difficulty.EASY);

        System.out.println(car1);
        System.out.println(car2);
        System.out.println(moto);
        System.out.println(trike);

        System.out.println("car1.equals(car2) -> " + car1.equals(car2));
        System.out.println("car1.equals(moto) -> " + car1.equals(moto));
    }
}
