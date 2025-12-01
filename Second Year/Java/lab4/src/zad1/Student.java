package zad1;

public class Student {
    private Integer age;
    private String name;
    private String group;

    public Student(){
        this.age = 0;
        this.name = "Default";
        this.group = "Default";
    }
    public Student(Integer age, String name, String group) {
        this.age = age;
        this.name = name;
        this.group = group;
    }

    @Override
    public String toString() {
        return "Student{" + "age=" + age + ", name='" + name + '\'' + ", group='" + group + '\'' +
                '}';
    }
}
