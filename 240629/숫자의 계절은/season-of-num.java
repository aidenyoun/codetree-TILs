import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        long m = sc.nextLong();

        if(m == 12 || m <= 2) {
            System.out.printf("Winter");
        }
        else if(m >= 9) System.out.printf("Fall");
        else if(m >= 6) System.out.printf("Summer");
        else if(m >= 3) System.out.printf("Spring");
    }
}