import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {

        int[] deploy = new int[progresses.length];
        
        for(int i = 0; i < progresses.length; i++){
            int remain = 100 - progresses[i];
            deploy[i] = (remain / speeds[i]) + (remain % speeds[i] == 0?0:1);
        }
        
        List<Integer> lst = new ArrayList<>();
        
        // 5일, 10일, 1일, 1일, 20일, 1일
        int before = deploy[0];
        int cnt = 0;
        for(int i = 0; i < deploy.length; i++){
            if(before >= deploy[i]){ // 이전 값 보다 작거나 같으면, cnt + 1
                cnt += 1;
            }else{ // 이전 값 보다 크면 cnt 1 부터 다시 시작, 이전 값 갱신
                lst.add(cnt);
                before = deploy[i]; 
                cnt = 1;
            }
        }
        if(cnt != 0) lst.add(cnt);
        
        int[] answer = new int[lst.size()];
        for(int i = 0; i < answer.length; i++){
            answer[i] = lst.get(i);
        }
        
        return answer;
    }
}