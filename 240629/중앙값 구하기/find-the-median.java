import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        long a = sc.nextLong();
        long b = sc.nextLong();
        long c = sc.nextLong();

        if ((a >= b && a <= c) || (a >= c && a <= b)) {
            System.out.printf("%d", a);
        } else if ((b >= a && b <= c) || (b >= c && b <= a)) {
            System.out.printf("%d", b);
        } else {
            System.out.printf("%d", c);
        }
    }
}