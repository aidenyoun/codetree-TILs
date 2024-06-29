import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        long a_math = sc.nextLong();
        long a_eng = sc.nextLong();
        long b_math = sc.nextLong();
        long b_eng = sc.nextLong();

        if(a_math > b_math) {
            System.out.printf("A");
        }
        else if(b_math > a_math) System.out.printf("B");
        else {
            if(a_eng > b_eng) System.out.printf("A");
            else if(b_eng > a_eng) System.out.printf("B");
        }
    }
}