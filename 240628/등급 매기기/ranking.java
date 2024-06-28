import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        long a = sc.nextLong();
        if (a >= 90) {
            System.out.printf("A");
        }
        else if (a >= 80) {
            System.out.printf("B");
        }
        else if (a >= 70) {
            System.out.printf("C");
        }
        else if (a >= 60) {
            System.out.printf("D");
        }        
        else System.out.printf("F");
    }
}