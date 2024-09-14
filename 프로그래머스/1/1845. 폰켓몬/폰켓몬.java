import java.util.*;
class Solution {
    public int solution(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        for(int num : nums){
            map.put(num, map.getOrDefault(num, 0) + 1);
        }
        int totalCnt = nums.length;
        int distinct = map.size();
        return Math.min(totalCnt / 2, distinct);
    }
}