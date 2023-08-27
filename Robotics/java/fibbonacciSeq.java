package Robotics.java;
public class fibbonacciSeq{
    public static void main(String[] args) {
        try {
            System.out.println(fib(50));
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }

    public static long fib(int n) throws Exception {
        long a = 0;
        long b = 1;

        if (n < 0) {
            throw new Exception("Error fib works w postive terms loll");
        } else if (n == 0) {
            return a;
        } else if (n == 1) {
            return b;
        } else {
            for (int i = 2; i <= n; i++) {
                long c = a + b;
                a = b;
                b = c;
            }
            return b;
        }
    }
}