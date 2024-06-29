import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        long a = sc.nextLong();
        long b = sc.nextLong();
        long c = sc.nextLong();
        long d = sc.nextLong();
        long e = sc.nextLong();

        if (a > b) {
            System.out.printf("1\n");
        }
        else System.out.printf("0\n");
        if (a > c) {
            System.out.printf("1\n");
        }
        else System.out.printf("0\n");
        if (a > d) {
            System.out.printf("1\n");
        }
        else System.out.printf("0\n");
        if (a > e) {
            System.out.printf("1\n");
        }
        else System.out.printf("0\n");                        
    }
}