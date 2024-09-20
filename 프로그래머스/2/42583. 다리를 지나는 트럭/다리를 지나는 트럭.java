import java.util.*;
import java.util.stream.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        int curWeight = 0;
        Queue<Integer> bridge = new LinkedList<>();
        
        for(int truck : truck_weights){
            while(true){
                if(bridge.size() == bridge_length){ // 길이 over
                    curWeight -= bridge.poll();
                }else if(curWeight + truck > weight){ // 무게 over
                    bridge.offer(0);
                    answer++;
                }else{
                    bridge.offer(truck);
                    curWeight += truck;
                    answer++;
                    break;
                }
            }
           
        }
        return answer + bridge_length;
    }
}