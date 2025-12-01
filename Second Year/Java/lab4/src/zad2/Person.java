package zad2;

public class Person {
    private Integer age;

    public Person(Integer age) {
        this.age = age;
    }

    public Integer getAge() {
        return age;
    }
    public void yearPases() {
        this.age++;
    }
    public String amIOld() {
        if (age <= 19) {
            return "Teenager";
        }
        else return "Adult";
    }
}
