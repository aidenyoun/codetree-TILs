import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        long b = sc.nextLong();
        long a = sc.nextLong();
        for (long i = b; i >= a; i-=2){
            System.out.printf("%d ", i);
        }
    }
}