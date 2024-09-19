import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String[] inputs = reader.readLine().split(" ");
        int N = Integer.parseInt(inputs[0]), K = Integer.parseInt(inputs[1]);
        int[] arr = Arrays.stream(reader.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        int start = 0;
        int answer = 0;

        Map<Integer, Integer> duplicateCount = new HashMap<>();

        for (int end = 0; end < N; end++) {
            duplicateCount.put(arr[end], duplicateCount.getOrDefault(arr[end], 0) + 1);

            // 5의 개수가 K보다 많다면
            while (duplicateCount.get(arr[end]) > K) {
                duplicateCount.put(arr[start], duplicateCount.get(arr[start]) - 1); // start 위치의 값을 하나 줄인다.
                if (duplicateCount.get(arr[start]) == 0) { // 줄였던 start 값의 개수가 0개라면
                    duplicateCount.remove(arr[start]); // 해당 값을 제거한다.
                }
                start++; // start 위치를 한칸 옮긴다.
            }

            answer = Math.max(answer, end - start + 1);
        }

        System.out.println(answer);
    }
}