import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        long h = sc.nextLong();
        long w = sc.nextLong();
        long b = (10000*w)/(h*h);
        System.out.printf("%d\n",b);
        if (b >= 25) {
            System.out.printf("Obesity");
        }
    }
}