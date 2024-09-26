import java.util.*;

class Solution {
    
    static ArrayList<Integer>[] adj;
    static int answer = 98;
    
    public int solution(int n, int[][] wires) {
        adj = new ArrayList[n+1];
        // [] 초기화
        for (int i = 1; i <= n; i++){
            adj[i] = new ArrayList<>();
        }
        // wires 를 adj에 삽입
        for (int i = 0; i < wires.length; i++){
            int a = wires[i][0];
            int b = wires[i][1];
            adj[a].add(b);
            adj[b].add(a);
        }
        
        // 노드 순회하면서 하나씩 끊고, 개수 세고, 다시 넣고
        for (int i = 0; i < wires.length; i++){
            // 끊고
            Integer a = wires[i][0];
            Integer b = wires[i][1];
            adj[a].remove(b);
            adj[b].remove(a);
            
            // 탐색
            boolean[] visited = new boolean[n+1];
            int cnt = dfs(1, visited);
            
            // 다시 넣고
            adj[a].add(b);
            adj[b].add(a);
            
            // 정답 갱신
            answer = Math.min(answer, Math.abs(cnt - (n - cnt)));
        }
        return answer;
    }
    
    static public int dfs(int v, boolean[] visited){
        int cnt = 1;
        visited[v] = true;
        
        for (int nxt : adj[v]){
            if(!visited[nxt]){
                cnt += dfs(nxt, visited);
            }
        }
        
        return cnt;
    }
}