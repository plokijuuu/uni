package zad3;

public class Main {
    public static void main(String[] args) {
        StringUtils utils = new StringUtils();

        System.out.println(utils.IsAnagram("abc", "abcd"));
        System.out.println(utils.IsAnagram("abab", "abba"));
        System.out.println(utils.IsAnagram("abcd", "abcc"));

    }
}
