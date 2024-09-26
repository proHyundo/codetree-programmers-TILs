

import java.util.*;
import java.io.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int[][] dxys = {
            {0, 1}, {1, 0}, {0, -1}, {-1, 0}
    };

    public static void main(String[] args) throws IOException{
        int testCase = 0;
        while (true){
            testCase++;
            int N = Integer.parseInt(br.readLine());
            if(N == 0){
                break;
            }
            // 초기화
            int[][] board = new int[N][N];
            for(int i = 0; i < N; i++){
                int[] temp = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
                board[i] = temp;
            }

            System.out.println("Problem " + testCase + ": " + bfs(N, board));
        }
    }

    public static int bfs(int N, int[][] board){
        Integer[] xys = {0, 0};
        Queue<Integer[]> q = new LinkedList<>();
        int[][] visited = new int[N][N];
        for(int i = 0; i < N; i++){
            Arrays.fill(visited[i], Integer.MAX_VALUE);
        }
        visited[0][0] = board[0][0];

        q.add(xys);

        while (!q.isEmpty()){
            Integer[] curXY = q.poll();
            int cx = curXY[0], cy = curXY[1];
            for (int[] dxy : dxys){
                int nx = cx + dxy[0], ny = cy + dxy[1];
                // 범위 내
                if(0 <= nx && nx < N && 0<= ny && ny < N){
                    if(visited[nx][ny] == Integer.MAX_VALUE || visited[nx][ny] > visited[cx][cy] + board[nx][ny]){ // 방문하지 않았거나, 방문했더라도 더 최솟 값이라면
                        // queue에 삽입하고, visited 갱신
                        visited[nx][ny] = visited[cx][cy] + board[nx][ny];
                        Integer[] nxy = {nx, ny};
                        q.add(nxy);
                    }
                }
            }

        }


        return visited[N-1][N-1];
    }

}
