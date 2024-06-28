import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        long a = sc.nextLong();
        if (a >= 3000) {
            System.out.printf("book");
        }
        else if (a >= 1000) {
            System.out.printf("mask");
        }
        else if (a >= 500) {
            System.out.printf("pen");
        }
        else System.out.printf("no");
    }
}