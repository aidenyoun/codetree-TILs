import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        if (a == "S") {
            System.out.printf("Superior");
        }
        else if (a == "A") {
            System.out.printf("Excellent");
        }
        else if (a == "B") {
            System.out.printf("Good");
        }
        else if (a == "C") {
            System.out.printf("Usually");
        }
        else if (a == "D") {
            System.out.printf("Effort");
        }        
        else System.out.printf("Failure");
    }
}