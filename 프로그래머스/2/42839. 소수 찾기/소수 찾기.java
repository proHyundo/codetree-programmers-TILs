import java.util.*;

class Solution {
    
    int answer = 0;
    int size = 0;
    String[] num_arr = null;
    static Set<Integer> primeSet = new HashSet<>();
    
    public int solution(String numbers) {
        this.num_arr = numbers.split("");
        this.size = num_arr.length;
        
        dfs(0, "", new boolean[size]);
        
        return this.answer;
    }
    
    public void dfs(int n, String num, boolean[] visited){
        if(n == size){
            if(!num.isEmpty()){
                int target = Integer.parseInt(num);
                if(!primeSet.contains(target) && isPrime(target)){
                    this.answer++;
                    primeSet.add(target);
                }
            }
            return;
        }
        
        for(int i = 0; i < this.size; i++){
            if(visited[i] == false){
                visited[i] = true;
                dfs(n+1, num + num_arr[i], visited);
                visited[i] = false;
                dfs(n+1, num, visited);
            }
        }
    }
    
    public boolean isPrime(int num){
        if (num < 2) return false;
        for(int i = 2; i <= Math.sqrt(num); i++){
            if (num % i == 0) return false;
        }
        return true;
    }
    
}