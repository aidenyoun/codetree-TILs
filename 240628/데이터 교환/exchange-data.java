public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        long a = 5, b = 6, c = 7;
        long temp = b;
        b = a;
        a = c;
        c = temp;
        System.out.printf("%d\n",a);
        System.out.printf("%d\n",b);
        System.out.printf("%d\n",c);
    }
}