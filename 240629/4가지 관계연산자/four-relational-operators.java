import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        long a = sc.nextLong();
        long b = sc.nextLong();
        if (a >= b) {
            System.out.printf("1\n");
        }
        else {
            System.out.printf("0\n");
        }
        if (a > b) {
            System.out.printf("1\n");
        }
        else {
            System.out.printf("0\n");
        }   
        if (b >= a) {
            System.out.printf("1\n");
        }
        else {
            System.out.printf("0\n");
        }
        if (b > a) {
            System.out.printf("1\n");
        }
        else {
            System.out.printf("0\n");
        }
    
    }
}