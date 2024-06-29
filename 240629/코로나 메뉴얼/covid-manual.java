import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String a1 = sc.next();
        long a2 = sc.nextLong();
        String b1 = sc.next();
        long b2 = sc.nextLong();
        String c1 = sc.next();
        long c2 = sc.nextLong();

        long A = 0;

        if (a1.equals("Y") && a2 >= 37) {
            A += 1;
        }
        if (b1.equals("Y") && b2 >= 37) {
            A += 1;
        }
        if (c1.equals("Y") && c2 >= 37) {
            A += 1;
        }
        if (A >= 2) System.out.printf("E");
        else System.out.printf("N");

    }
}