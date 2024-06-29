import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        long sex = sc.nextLong();
        long age = sc.nextLong();
        if (sex == 0) {
            if (age >= 19) System.out.printf("MAN");
            else System.out.printf("BOY");
        }
        else {
            if (age >= 19) System.out.printf("WOMAN");
            else System.out.printf("GIRL");
        }
    }
}