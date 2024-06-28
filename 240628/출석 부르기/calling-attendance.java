import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        long a = sc.nextLong();
        if (a == 1) {
            System.out.printf("John");
        }
        else if (a == 2) {
            System.out.printf("Tom");
        }
        else if (a == 3) {
            System.out.printf("Paul");
        }
        else System.out.printf("Vacnacy");
    }
}