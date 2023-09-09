package Robotics.java;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class conv {

    public static List<Double> averageConvolution(List<Double> data, int k) {
        List<Double> kernel = IntStream.range(0, k).mapToObj(i -> 1.0 / k).collect(Collectors.toList());
        int paddingSize = (k - 1) / 2;
        List<Double> paddedData = new ArrayList<>();

        for (int i = 0; i < paddingSize; i++) {
            paddedData.add(0.0);
        }
        paddedData.addAll(data);
        for (int i = 0; i < paddingSize; i++) {
            paddedData.add(0.0);
        }

        List<Double> result = new ArrayList<>();
        for (int i = 0; i < data.size(); i++) {
            List<Double> segment = paddedData.subList(i, i + k);
            double averagedValue = IntStream.range(0, k)
                    .mapToDouble(j -> segment.get(j) * kernel.get(j))
                    .sum();
            result.add(averagedValue);
        }
        return result;
    }

    public static void main(String[] args) {
        List<Double> data = Arrays.asList(2.0, 3.0, 4.0, 5.0, 6.0);
        int ksize = 3;
        List<Double> cdata = averageConvolution(data, ksize);
        System.out.println("data: " + cdata);
    }
}
