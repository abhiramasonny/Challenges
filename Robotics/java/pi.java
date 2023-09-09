package Robotics.java;

import java.util.Random;

public class pi {
        public static void main(String[] args) {
        Random randomThing = new Random();

        long allPoints = 0;
        long pointsInCircle = 0;

        for (long count = 0; count < 10000L; count++) {
            double xPoint = randomThing.nextDouble() * 2 - 1;  
            double yPoint = randomThing.nextDouble() * 2 - 1;  

            allPoints++;

            if (xPoint * xPoint + yPoint * yPoint <= 1) {
                pointsInCircle++;
            }
        }

        double piGuess = 4.0 * pointsInCircle / allPoints;
        System.out.println(piGuess);
    }
}
