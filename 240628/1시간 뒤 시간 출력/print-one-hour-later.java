import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        sc.useDelimiter(":");
        long a = sc.nextLong();
        long b = sc.nextLong();
        System.out.printf("%d:%d",a+1,b);
    }
}