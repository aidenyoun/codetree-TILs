import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        long a_age = sc.nextLong();
        String a_sex = sc.next();
        long b_age = sc.nextLong();
        String b_sex = sc.next();
        if ((a_age >= 19 && a_sex.equals("M")) || (b_age >= 19 && b_sex.equals("M"))) {
            System.out.printf("1");
        }
        else System.out.printf("0");
    }
}