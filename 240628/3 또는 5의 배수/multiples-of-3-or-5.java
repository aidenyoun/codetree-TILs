import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        long a = sc.nextLong();
        if (a % 3 == 0) {
            System.out.printf("YES\n");
        }
        else {
            System.out.printf("NO\n");
        }
        if (a % 5 == 0) {
            System.out.printf("YES");
        }
        else {
            System.out.printf("NO");
        }        
    }
}