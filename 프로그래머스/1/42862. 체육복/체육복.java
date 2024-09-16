import java.util.*;
import java.util.stream.*;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        HashSet<Integer> t_lost = Arrays.stream(lost).boxed().collect(Collectors.toCollection(HashSet::new));
        HashSet<Integer> t_reserve = Arrays.stream(reserve).boxed().collect(Collectors.toCollection(HashSet::new));
        
        HashSet<Integer> s_lost = new HashSet(t_lost);
        s_lost.removeAll(t_reserve);
        
        HashSet<Integer> s_reserve = new HashSet(t_reserve);
        s_reserve.removeAll(t_lost);
        
        int answer = n - s_lost.size();
        for(int l : s_lost){
            if(s_reserve.contains(l-1)){
                s_reserve.remove(l-1);
                answer += 1;
            }else if(s_reserve.contains(l+1)){
                s_reserve.remove(l+1);
                answer += 1;
            }
            
        }

        return answer;
    }
}