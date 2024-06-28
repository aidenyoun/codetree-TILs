import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        long a = sc.nextLong();
        if (a >= 113) {
            System.out.printf("1");
        }
        else {
            System.out.printf("0");
        }
    }
}