import java.util.Scanner;

public class Main {
    public static void main (String args[]) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        double b = sc.nextDouble();
        double c = sc.nextDouble();

        System.out.printf("%s\n",a);
        System.out.printf("%.5f\n",b);
        System.out.printf("%.4f",c);
    }
}