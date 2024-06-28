import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        long a = sc.nextLong();
        long b = sc.nextLong();
        a += 8;
        b *= 3;
        System.out.printf("%d\n",a);
        System.out.printf("%d\n",b);
        System.out.printf("%d",a*b);
    }
}