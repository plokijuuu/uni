package zad6;

public class ATMService {
    private Integer tens;
    private Integer twenties;
    private Integer fifties;
    private Integer hundreds;
    private Integer twoHundreds;
    private Integer fiveHundreds;

    public ATMService() {
        this.tens = 0;
        this.twenties = 0;
        this.fifties = 0;
        this.hundreds = 0;
        this.twoHundreds = 0;
        this.fiveHundreds = 0;
    }

    private int getAmount() {
        return this.tens * 10 + this.twenties * 20 + this.fifties * 50 + this.hundreds * 100 + this.twoHundreds * 200 + this.fiveHundreds * 500;
    }

    public void deposit(int nom, int amount) {
        switch (nom) {
            case 10:
                this.tens += amount;
                break;
            case 20:
                this.twenties += amount;
                break;
            case 50:
                this.fifties += amount;
                break;
            case 100:
                this.hundreds += amount;
                break;
            case 200:
                this.twoHundreds += amount;
                break;
            case 500:
                this.fiveHundreds += amount;
                break;
            default:
                System.out.println("Nie przyjmuję takiego nominału.");
                break;
        }
    }

    private boolean backtrack(int remaining, int[] denoms, int[] counts, int[] used, int index) {
        if (remaining == 0) return true;
        if (index == denoms.length) return false;

        int denom = denoms[index];
        int available = counts[index];
        int maxNeeded = remaining / denom;

        int limit = Math.min(available, maxNeeded);

        for (int i = limit; i >= 0; i--) {
            used[index] = i;
            int newRemaining = remaining - i * denom;

            if (backtrack(newRemaining, denoms, counts, used, index + 1)) {
                return true;
            }
        }

        used[index] = 0;
        return false;
    }

    public void withdraw(int amount) {
        if(amount > this.getAmount()) {
            System.out.println("Bankomat nie posiada wystarczająco środków.");
            return;
        }
        else if(amount < 0 || amount % 10 != 0) {
            System.out.println("Nie poprawna kwota.");
            return;
        }

        int[] denoms = {500, 200, 100, 50, 20, 10};

        int[] counts = {
                this.fiveHundreds,
                this.twoHundreds,
                this.hundreds,
                this.fifties,
                this.twenties,
                this.tens
        };

        int[] used = new int[denoms.length];

        boolean ok = backtrack(amount, denoms, counts, used, 0);

        if (!ok) {
            System.out.println("Nie mogę wypłacić tej kwoty dostępnymi nominałami.");
            return;
        }

        this.fiveHundreds -= used[0];
        this.twoHundreds -= used[1];
        this.hundreds -= used[2];
        this.fifties -= used[3];
        this.twenties -= used[4];
        this.tens -= used[5];

        System.out.println("Wypłacono " + amount + ":");
        for (int i = 0; i < denoms.length; i++) {
            if (used[i] > 0) {
                System.out.println(denoms[i] + " zł x " + used[i]);
            }
        }
    }
}

