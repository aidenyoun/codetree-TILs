public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        long a = 2;
        long b = 5;
        long temp;
        temp = b;
        b = a;
        a = temp;
        System.out.printf("%d\n",a);
        System.out.printf("%d",b);
    }
}