import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int N, D, K, C;
    static int answer;

    public static void main(String[] args) throws IOException {
        int[] input = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        N = input[0]; // 접시의 수
        D = input[1]; // 초밥의 가짓수
        K = input[2]; // 연속해서 먹는 접시의 수
        C = input[3]; // 쿠폰 번호
        answer = 0;

        ArrayList<Integer> sushi = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            sushi.add(Integer.parseInt(br.readLine()));
        }

        // 30,000 * 3,000 : 900,000
        for (int i = 0; i <= N-K; i++){
//            System.out.println("i : " + i + " \t i+K : " + (i+K));
            HashSet<Integer> set = new HashSet<>(sushi.subList(i, i + K));
            if(set.contains(C)){ // 쿠폰 초밥을 포함
                answer = Math.max(answer, set.size());
            }else{
                answer = Math.max(answer, set.size() + 1);
            }
        }

        for (int i = N-K+1; i < N; i++){
//            System.out.println("i : " + i + " \t K - (N-i) : " + (K - (N-i)));
            HashSet<Integer> set = new HashSet<>(sushi.subList(i, N));
            set.addAll(sushi.subList(0, K - (N-i)));
            if(set.contains(C)){ // 쿠폰 초밥을 포함
                answer = Math.max(answer, set.size());
            }else{
                answer = Math.max(answer, set.size() + 1);
            }
        }

        System.out.println(answer);

    }
}
