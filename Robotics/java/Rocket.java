package Robotics.java;
import java.util.Arrays;

public class Rocket {
    public static void main(String[] args) {
        double[] v = new double[20];
        for (int i = 0; i < 20; i++) {
            v[i] = i + 1;
        }
        
        double dt = 0.2;
        double distance = computeDistance(v, dt);
        double[] acceleration = computeAcc(v, dt);
        
        System.out.println("aprx distance: " + distance);
        System.out.println("aprx acceleration: " + Arrays.toString(acceleration));
    }

    public static double computeDistance(double[] v, double dt) {
        double sum = 0;
        for (double value : v) {
            sum += value;
        }
        return sum * dt;
    }

    public static double[] computeAcc(double[] v, double dt) {
        int n = v.length;
        double[] a = new double[n];
        
        for (int i = 1; i < n - 1; i++) {
            a[i] = (v[i + 1] - v[i - 1]) / (2 * dt);
        }
        
        a[0] = (v[1] - v[0]) / dt;
        a[n - 1] = (v[n - 1] - v[n - 2]) / dt;
        
        return a;
    }
}
