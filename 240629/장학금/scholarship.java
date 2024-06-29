import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        long m = sc.nextLong();
        long f = sc.nextLong();

        if(m < 90) {
            System.out.printf("0");
        }
        else if(f >= 95) System.out.printf("100000");
        else if(f >= 90) System.out.printf("50000");
        else System.out.printf("0");
    }
}