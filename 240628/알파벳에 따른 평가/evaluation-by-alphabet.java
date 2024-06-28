import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        if (a.equals("S")) {
            System.out.printf("Superior");
        }
        else if (a.equals("A")) {
            System.out.printf("Excellent");
        }
        else if (a.equals("B")) {
            System.out.printf("Good");
        }
        else if (a.equals("C")) {
            System.out.printf("Usually");
        }
        else if (a.equals("D")) {
            System.out.printf("Effort");
        }        
        else System.out.printf("Failure");
    }
}