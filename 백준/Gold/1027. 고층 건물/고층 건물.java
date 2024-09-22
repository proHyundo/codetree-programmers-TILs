import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int N;
    static int answer = 0;

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(br.readLine());
        int[] buildings = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        // 모든 빌딩 순회
        for (int i = 0; i < N; i++){
            int cnt = 0;

            // 타겟 빌딩의 왼쪽을 탐색 : 기울기가 점점 감소해야 함
            double leftScope = Integer.MAX_VALUE;
            for (int j = i-1; j >= 0; j--){
                double temp = (double) (buildings[i] - buildings[j]) / (i-j);
                if(temp < leftScope){ // 기울기가 감소하면 ++
                    leftScope = temp;
                    cnt++;
                }
            }

            // 타겟 빌딩의 오른쪽을 탐색 : 기울기가 점점 증가해야 함
            double rightScope = Integer.MIN_VALUE;
            for (int j = i+1; j < N; j++){
                double temp = (double) (buildings[i] - buildings[j]) / (i-j);
                if(temp > rightScope){ // 기울기가 증가하면 ++
                    rightScope = temp;
                    cnt++;
                }
            }
            answer = Math.max(answer, cnt);
        }

        System.out.println(answer);
    }
}
