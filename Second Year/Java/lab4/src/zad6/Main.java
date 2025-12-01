package zad6;

public class Main {
    public static void main(String[] args) {
        ATMService atmService = new ATMService();
        atmService.deposit(500,1);
        atmService.deposit(200,3);
        atmService.withdraw(600);
    }
}
