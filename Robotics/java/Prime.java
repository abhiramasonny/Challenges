package Robotics.java;

public class Prime {

    private int n;

    public Prime(int n) {
        this.n = n;
        System.out.println(check(n));
    }

    private boolean check(int n) {
        if (n < 2) {
            return false;
        }
        if (n % 2 == 0 && n != 2) {
            return false;
        }
        if (n % 3 == 0 && n != 3) {
            return false;
        }
        int i = 5;
        int w = 2;
        while (i * i <= n) {
            if (n % i == 0) {
                return false;
            }
            i += w;
            w = 6 - w;
        }
        return true;
    }

    public static void main(String[] args) {
        Prime p = new Prime(29);
    }
}
