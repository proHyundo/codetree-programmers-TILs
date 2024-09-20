

import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

class Adj<W, V> {
    public V v;
    public W weight;

    public Adj(V v, W weight) {
        this.v = v;
        this.weight = weight;
    }

    public String toString() {
        return "weight: " + weight + ", v: " + v;
    }
}

public class Main {

    static BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    static int N, M, J, K;
    static ArrayList<Integer> aLst, bLst;
    static int[] visited;

    public static void main(String[] args) throws Exception {

        String[] inputs = reader.readLine().split(" ");
        N = Integer.parseInt(inputs[0]);
        M = Integer.parseInt(inputs[1]); // N: 집 개수, M: 길 개수
        J = Integer.parseInt(reader.readLine()); // J: 출발 집 번호
        K = Integer.parseInt(reader.readLine()); // K: 동물 수

        // string[] -> int[] -> List<Integer>
        aLst = Arrays.stream(reader.readLine().split(" ")).mapToInt(Integer::parseInt).boxed().collect(Collectors.toCollection(ArrayList::new));
        bLst = Arrays.stream(reader.readLine().split(" ")).mapToInt(Integer::parseInt).boxed().collect(Collectors.toCollection(ArrayList::new));

        // 방문 배열 초기화
        visited = new int[N + 1];
        Arrays.fill(visited, Integer.MAX_VALUE);

        // 인접 리스트 생성 및 초기화
        ArrayList<ArrayList<Adj<Integer, Integer>>> adj = new ArrayList<>();
        for (int i = 0; i <= N; i++) {
            adj.add(new ArrayList<>());
        }
        for (int i = 0; i < M; i++) { // 간선의 갯수만큼 반복
            String[] edge = reader.readLine().split(" ");
            int n1 = Integer.parseInt(edge[0]), n2 = Integer.parseInt(edge[1]), weight = Integer.parseInt(edge[2]);
            adj.get(n1).add(new Adj<>(n2, weight));
            adj.get(n2).add(new Adj<>(n1, weight));
        }

        // BFS 인접리스트 탐색 -> visited 배열에 거리 저장
        bfs(J, visited, adj);


        // 최소 거리 찾기
        int min_a = Integer.MAX_VALUE;
        int min_b = Integer.MAX_VALUE;

        for (int i = 0; i < K; i++) {
            min_a = Math.min(min_a, visited[aLst.get(i)]);
            min_b = Math.min(min_b, visited[bLst.get(i)]);
        }

        // 최소 거리 출력
        if (min_a == Integer.MAX_VALUE && min_b == Integer.MAX_VALUE) {
            System.out.println(-1);
        } else if(min_a <= min_b){
            System.out.println("A");
            System.out.println(min_a);
        } else {
            System.out.println("B");
            System.out.println(min_b);
        }

    }

    public static void bfs(int startJ, int[] visited, ArrayList<ArrayList<Adj<Integer, Integer>>> adj){
        Queue<Integer> q = new LinkedList<>();
        q.add(startJ);
        visited[startJ] = 0;
        while (!q.isEmpty()) {
            int cur = q.poll();
            // 너비우선 탐색
            for (Adj<Integer, Integer> next : adj.get(cur)) {
                if (visited[next.v] > visited[cur] + next.weight) {
                    visited[next.v] = visited[cur] + next.weight;
                    q.add(next.v);
                }
            }
        }
    }
}