import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        // 주어진 배열을 큐로 변환
        PriorityQueue<Integer> pq = new PriorityQueue(Collections.reverseOrder());
        for(int num : priorities) {
			pq.add(num);
		}
        while(!pq.isEmpty()){
            for(int i= 0; i<priorities.length; i++){
                if(priorities[i] == pq.peek()){
                    answer++;
                    pq.poll();
                    if(i==location){
                        return answer;
                    }
                }
                
            }
        }
        return answer;
    }
}